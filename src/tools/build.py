#!/usr/bin/env python3
"""Assemble Lexicourse en UN seul fichier HTML autonome (images intégrées).
Usage, depuis la racine du dépôt :  python src/tools/build.py
Entrées : src/template.html, src/questions/*.json, assets/sources/**   Sortie : index.html"""
import json, base64, io, os, numpy as np
from pathlib import Path
from PIL import Image
from scipy import ndimage as ndi

ROOT = Path(__file__).resolve().parents[2]; SRC = ROOT/'assets'/'sources'; K = 1.5   # K = netteté des sprites (1,5 × la taille d'écran)

# ---- Personnages : (nom affiché, dossier, images de transformation gardées, 2 rangées ?, hauteur max à l'écran en px, finesse de détection)
PERSOS = [('Rouge','rouge',[0,1,4,5,6,7],True,230,12), ('Jaune','jaune',[0,1,2,3,5,6,7],True,230,12),
          ('Bleu (camion)','camion',None,False,290,5), ('Noir (moto)','moto',None,False,250,12)]
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
    p,sh = parts(path, it)
    p = (sorted([q for q in p if q[1] < sh[0]/2], key=lambda q: q[0]) + sorted([q for q in p if q[1] >= sh[0]/2], key=lambda q: q[0])) if two else sorted(p, key=lambda q: q[0])
    return [q[2] for q in p]

def rs(im, s): return im.resize((max(1,round(im.width*s)), max(1,round(im.height*s))), Image.LANCZOS)
def b64(im): b = io.BytesIO(); im.save(b,'WEBP',quality=90,method=4); return 'data:image/webp;base64,'+base64.b64encode(b.getvalue()).decode()
def find(folder, stem): return next((SRC/folder).glob(stem+'.*'))

def main():
    A = {'k':K,'roadside':[],'obst':[],'chars':[]}; D = 'decors/piste1-cyber-city'
    b = io.BytesIO(); Image.open(find(D,'ciel-panorama')).convert('RGB').crop((0,0,664,512)).save(b,'PNG',optimize=True); A['bg'] = 'data:image/png;base64,'+base64.b64encode(b.getvalue()).decode()
    P,_ = parts(find(D,'bord-de-route'), 5, 40)
    for r,(lo,hi) in enumerate([(0,384),(384,768)]):
        for nm,q in zip(['pylon','lamp','billboard','house','tree','barrier','chevron','light'], sorted([q for q in P if lo <= q[1] < hi], key=lambda q: q[0])):
            im = q[2]
            if nm == 'lamp':   # le faisceau du lampadaire est semi-transparent : on le retire
                ar = np.array(im).astype(int); m = (ar[...,1] > ar[...,2]+10) & (ar[...,1] > ar[...,0]+60); ar[...,3][m] = 0; im = Image.fromarray(ar.astype(np.uint8),'RGBA')
            A['roadside'].append({'n':nm+'_'+'ab'[r], 'u':b64(rs(im,300/im.height) if im.height > 300 else im), 'hh':HH[nm]})
    P,_ = parts(find(D,'obstacles'), 12, 60); r1 = sorted([q for q in P if q[1] < 384], key=lambda q: q[0]); r2 = sorted([q for q in P if q[1] >= 384], key=lambda q: q[0])
    for nm,q in {'barrier':r1[0],'blocks':r1[2],'pool':r2[0],'ramp':r2[1]}.items(): A['obst'].append({'n':nm,'u':b64(rs(q[2],220/q[2].height)),'ww':WW[nm]})
    for lab,dossier,idx,two,h,it in PERSOS:
        T = ordered(find('personnages/'+dossier,'transformation-dos'), two, it); T = [T[i] for i in idx] if idx else T
        s = h*K/max(T[0].height, T[-1].height); Ts = [rs(t,s) for t in T]
        Js = [rs(j, Ts[0].width/j.width) for j in ordered(find('personnages/'+dossier,'saut'))[:3]]
        Ss = [rs(q, Ts[-1].height/q.height) for q in ordered(find('personnages/'+dossier,'enjambement'))[:3]]
        print(lab, '| transformation', len(Ts), '| saut', len(Js), '| enjambement', len(Ss))
        A['chars'].append({'label':lab,'tr':[b64(i) for i in Ts],'jump':[b64(i) for i in Js],'step':[b64(i) for i in Ss]})
    bank = json.load(open(ROOT/'src'/'questions'/'consignes.json', encoding='utf-8'))
    Q = [[q['question'], q['options'], q['bonne_reponse'], q['explication']] for q in bank]
    html = (ROOT/'src'/'template.html').read_text(encoding='utf-8').replace('/*ASSETS*/', json.dumps(A,separators=(',',':'))).replace('/*QUESTIONS*/', json.dumps(Q,ensure_ascii=False))
    (ROOT/'index.html').write_text(html, encoding='utf-8'); print('index.html :', os.path.getsize(ROOT/'index.html')//1024, 'Ko')

if __name__ == '__main__': main()
