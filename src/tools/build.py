#!/usr/bin/env python3
"""Assemble Lexicourse en UN seul fichier HTML autonome (images intégrées).
Usage, depuis la racine du dépôt :  python src/tools/build.py
Entrées : src/template.html, src/questions/*.json, assets/sources/**   Sortie : index.html"""
import json, base64, io, os, numpy as np
from pathlib import Path
from PIL import Image
from scipy import ndimage as ndi
sys_path = None
import sys; sys.path.insert(0, str(Path(__file__).resolve().parent))
import cartes

ROOT = Path(__file__).resolve().parents[2]; SRC = ROOT/'assets'/'sources'; K = 1.5   # K = netteté des sprites (1,5 × la taille d'écran)

# Les personnages sont décrits dans src/personnages.json (nom, dossier, famille, couleur, rareté, hauteur à l'écran…)
HH = {'pylon':3200,'lamp':2600,'billboard':2200,'house':1700,'tree':2600,'barrier':520,'chevron':420,'light':2600}   # hauteur dans le monde du jeu
WW = {'barrier':900,'blocks':750,'pool':950,'ramp':900}                                                           # largeur des obstacles

def keyimg(path, tol=70, tight=30, minarea=400):
    """Retire le fond uni (vert/bleu) en partant des bords ; supprime les petites taches (textes, traits)."""
    im = np.array(Image.open(path).convert('RGB')).astype(int)
    bg = np.median(np.concatenate([im[0],im[-1],im[:,0],im[:,-1]]), axis=0); d = np.sqrt(((im-bg)**2).sum(2))
    if bg[1] > 230 and bg[0] < 40 and bg[2] < 40: tol = 115          # vert vif : on retire aussi l'ombre vert foncé
    lab,_ = ndi.label(d < tol); e = set(np.unique(np.r_[lab[0],lab[-1],lab[:,0],lab[:,-1]])) - {0}
    bgm = np.isin(lab, list(e)) | (d < tight); near = ndi.binary_dilation(bgm, iterations=2) & ~bgm
    k = int(np.argmax(bg)); o = [c for c in range(3) if c != k]; lim = np.maximum(im[...,o[0]], im[...,o[1]])
    im[...,k] = np.where(near & (im[...,k] > lim), lim, im[...,k])
    if bg[0] > 180 and bg[2] > 180 and bg[1] < 90:   # fond magenta : on ramène le rouge parasite des contours
        im[...,0] = np.where(near & (im[...,0] > im[...,1]), im[...,1], im[...,0])
    al = ~bgm; l2,n = ndi.label(al); ar = ndi.sum(al, l2, range(1,n+1)); al = np.isin(l2, [i+1 for i,a in enumerate(ar) if a >= minarea])
    return np.dstack([im.clip(0,255).astype(np.uint8), al.astype(np.uint8)*255])

def parts(path, it=12, minh=100):
    a = keyimg(path); l,_ = ndi.label(ndi.binary_dilation(a[...,3] > 0, iterations=it)); out = []
    for i,s in enumerate(ndi.find_objects(l)):
        if s[0].stop-s[0].start <= minh: continue
        b = a.copy(); b[...,3] = np.where(l == i+1, b[...,3], 0); im = Image.fromarray(b[s],'RGBA'); bb = im.getbbox()
        if bb: out.append(((s[1].start+s[1].stop)/2, (s[0].start+s[0].stop)/2, im.crop(bb)))
    return out, a.shape

def ordered(path, two=False, it=12):
    """Images détectées, dans l'ordre de lecture (ligne par ligne, de gauche à droite), quel que soit le nombre de rangées."""
    p,_ = parts(path, it)
    if not p: return []
    hs = sorted(q[2].height for q in p); med = hs[len(hs)//2]; p.sort(key=lambda q: q[1]); rows = [[p[0]]]
    for q in p[1:]:
        (rows[-1].append(q) if q[1]-rows[-1][-1][1] <= med*.55 else rows.append([q]))
    return [q[2] for row in rows for q in sorted(row, key=lambda q: q[0])]

def ordered_auto(path, expected, two=False):
    """Détections de plus en plus fines jusqu'à retrouver le bon nombre d'images (images collées) ; garde les plus grandes (écarte traits et taches)."""
    for it in (12, 8, 5, 3):
        r = ordered(path, two, it)
        if len(r) >= expected:
            keep = sorted(sorted(range(len(r)), key=lambda i: -r[i].width*r[i].height)[:expected])
            return [r[i] for i in keep]
    return split_widest(r, expected) if not two else r

def split_widest(r, expected):
    """Deux images qui se touchent : on coupe la plus large à l'endroit le plus étroit."""
    r = list(r)
    while 0 < len(r) < expected:
        i = max(range(len(r)), key=lambda k: r[k].width); im = r[i]
        col = (np.array(im)[...,3] > 0).sum(0); lo, hi = int(im.width*.3), int(im.width*.7); cut = lo + int(np.argmin(col[lo:hi]))
        r[i:i+1] = [p.crop(p.getbbox()) for p in (im.crop((0,0,cut,im.height)), im.crop((cut,0,im.width,im.height))) if p.getbbox()]
    return r

def rs(im, s): return im.resize((max(1,round(im.width*s)), max(1,round(im.height*s))), Image.LANCZOS)
def b64(im): b = io.BytesIO(); im.save(b,'WEBP',quality=90,method=4); return 'data:image/webp;base64,'+base64.b64encode(b.getvalue()).decode()
def find(folder, stem): return next((SRC/folder).glob(stem+'.*'))

def card_for(e, persos):
    """Deux images de carte : complète (voiture devant + robot derrière) et « voiture seule » (avant la découverte du robot).
    Une carte faite à la main (carte.*) n'est utilisée que si l'entrée JSON contient "carte":"main"."""
    typ = e.get('type','energie'); base = next(p for p in persos if p['id'] == e.get('sprites_de', e['id']))
    out = ROOT/'assets'/'generated'/'cartes'; out.mkdir(parents=True, exist_ok=True)
    hand = next((SRC/'personnages'/e['dossier']).glob('carte.*'), None) if e.get('carte') == 'main' else None
    fiche = next((SRC/'personnages'/base['dossier']).glob('fiche.*'), None)
    if fiche and not (e.get('sprites_de') and hand):
        v = ordered_auto(fiche, 8); fond = SRC/'cartes'/'fonds'/(typ+'.png')
        full = cartes.compose(fond, v[1], v[4], typ); car = cartes.compose(fond, v[1], v[4], typ, False); car.save(out/(e['id']+'-voiture.png'))
    else: full = car = None
    if hand: full = Image.open(hand).convert('RGB')
    full.save(out/(e['id']+'.png')); full = full.resize((340,510), Image.LANCZOS)
    return b64(full), (b64(car.resize((340,510), Image.LANCZOS)) if car is not None else None)

def main():
    A = {'k':K,'roadside':[],'obst':[],'chars':[]}; D = 'decors/piste1-cyber-city'
    b = io.BytesIO(); Image.open(find(D,'ciel-panorama')).convert('RGB').crop((0,0,664,512)).save(b,'PNG',optimize=True); A['bg'] = 'data:image/png;base64,'+base64.b64encode(b.getvalue()).decode()
    A['home'] = b64(Image.open(SRC/'interface'/'accueil.png').convert('RGB').resize((1280,720), Image.LANCZOS))   # écran d'accueil
    P,_ = parts(find(D,'bord-de-route'), 5, 40)
    for r,(lo,hi) in enumerate([(0,384),(384,768)]):
        for nm,q in zip(['pylon','lamp','billboard','house','tree','barrier','chevron','light'], sorted([q for q in P if lo <= q[1] < hi], key=lambda q: q[0])):
            im = q[2]
            if nm == 'lamp':   # le faisceau du lampadaire est semi-transparent : on le retire
                ar = np.array(im).astype(int); m = (ar[...,1] > ar[...,2]+10) & (ar[...,1] > ar[...,0]+60); ar[...,3][m] = 0; im = Image.fromarray(ar.astype(np.uint8),'RGBA')
            A['roadside'].append({'n':nm+'_'+'ab'[r], 'u':b64(rs(im,300/im.height) if im.height > 300 else im), 'hh':HH[nm]})
    P,_ = parts(find(D,'obstacles'), 12, 60); r1 = sorted([q for q in P if q[1] < 384], key=lambda q: q[0]); r2 = sorted([q for q in P if q[1] >= 384], key=lambda q: q[0])
    for nm,q in {'barrier':r1[0],'blocks':r1[2],'pool':r2[0],'ramp':r2[1]}.items(): A['obst'].append({'n':nm,'u':b64(rs(q[2],220/q[2].height)),'ww':WW[nm]})
    persos = json.load(open(ROOT/'src'/'personnages.json', encoding='utf-8'))
    done = {}; RAR = {1:'commune',2:'commune',3:'rare',4:'epique',5:'extra'}
    for e in persos:
        lab,dossier,idx,two,h = e['nom'],e['dossier'],e.get('indices'),e.get('deux_rangees',False),e['hauteur']
        meta = {'id':e['id'],'label':lab,'famille':e.get('famille',e['id']),'couleur':e.get('couleur','#ffffff'),'etoiles':e.get('etoiles',2),'type':e.get('type','energie'),'rarete':'depart' if e.get('depart') else RAR[e.get('etoiles',2)],'part':e.get('particularite','')}
        meta['card'], meta['cardCar'] = card_for(e, persos)
        if e.get('sprites_de'):   # même sprites qu'un autre personnage (en attendant les siens)
            A['chars'].append(dict(done[e['sprites_de']], **meta)); continue
        T = ordered_auto(find('personnages/'+dossier,'transformation-dos'), (max(idx)+1 if idx else 6), two); T = [T[i] for i in idx] if idx else T
        s = h*K/max(T[0].height, T[-1].height); Ts = [rs(t,s) for t in T]
        Js = [rs(j, Ts[0].width/j.width) for j in ordered_auto(find('personnages/'+dossier,'saut'), 3)[:3]]
        Ss = [rs(q, Ts[-1].height/q.height) for q in ordered_auto(find('personnages/'+dossier,'enjambement'), 3)[:3]]
        print(lab, '| transformation', len(Ts), '| saut', len(Js), '| enjambement', len(Ss))
        ch = dict(meta, tr=[b64(i) for i in Ts], jump=[b64(i) for i in Js], step=[b64(i) for i in Ss]); A['chars'].append(ch); done[e['id']] = ch
    cfg = ROOT/'firebase'/'firebase.config.json'   # configuration Firebase web (facultative ; pas un secret, la sécurité est dans les règles)
    if cfg.exists(): A['firebase'] = json.load(open(cfg, encoding='utf-8'))
    bank = json.load(open(ROOT/'src'/'questions'/'consignes.json', encoding='utf-8'))
    Q = [[q['question'], q['options'], q['bonne_reponse'], q['explication']] for q in bank]
    html = (ROOT/'src'/'template.html').read_text(encoding='utf-8').replace('/*ASSETS*/', json.dumps(A,separators=(',',':'))).replace('/*QUESTIONS*/', json.dumps(Q,ensure_ascii=False))
    if os.environ.get('LEXI_CHECK'):   # aperçu de contrôle des personnages : tests/apercu_personnages.png
        sh = Image.new('RGB',(2600,len(A['chars'])*300),(110,40,150))
        for r,c in enumerate(A['chars']):
            x = 0
            for im in [Image.open(io.BytesIO(base64.b64decode(u.split(',')[1]))) for u in c['tr']+c['jump']+c['step']]:
                im = rs(im, min(1,280/im.height)); sh.paste(im,(x,r*300),im); x += im.width+6
        sh.save(ROOT/'tests'/'apercu_personnages.png')
    (ROOT/'index.html').write_text(html, encoding='utf-8'); print('index.html :', os.path.getsize(ROOT/'index.html')//1024, 'Ko')

if __name__ == '__main__': main()
