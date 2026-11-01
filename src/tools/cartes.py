"""Composition automatique des cartes : fond du type + voiture de face (derrière) + robot de face (devant), d'après la planche 8 vues.
Le nom et les étoiles ne sont PAS dessinés ici : le jeu les ajoute (nom en bas, étoiles en haut à gauche)."""
from PIL import Image, ImageDraw, ImageFilter
CW, CH = 1027, 1536
GLOW = {'feu':(255,70,40),'electrique':(255,230,60),'energie':(80,255,140),'eau':(60,170,255),'force':(255,150,30),'glace':(120,190,255),'love':(255,120,170),'nature':(110,220,90),'tenebre':(40,230,230)}

def fit(im, max_w, max_h):
    s = min(max_w/im.width, max_h/im.height); return im.resize((max(1,round(im.width*s)), max(1,round(im.height*s))), Image.LANCZOS)

def _fond(fond, typ):
    bg = Image.open(fond).convert('RGBA').resize((CW, CH), Image.LANCZOS)
    glow = Image.new('RGBA', (CW, CH), (0,0,0,0)); ImageDraw.Draw(glow).ellipse((CW//2-340, int(CH*.14), CW//2+340, int(CH*.78)), fill=GLOW.get(typ,(255,255,255))+(105,))
    return Image.alpha_composite(bg, glow.filter(ImageFilter.GaussianBlur(120)))

def _ombre(bg, y, largeur):
    sh = Image.new('RGBA', (CW, CH), (0,0,0,0)); ImageDraw.Draw(sh).ellipse((CW//2-largeur//2, y-24, CW//2+largeur//2, y+24), fill=(0,0,0,160))
    return Image.alpha_composite(bg, sh.filter(ImageFilter.GaussianBlur(14)))

def compose(fond, car34, robot, typ, avec_robot=True):
    """Voiture de 3/4 avant DEVANT ; robot de face DERRIÈRE (absent si avec_robot est faux : la surprise du tutoriel)."""
    bg = _fond(fond, typ)
    if avec_robot:
        r = fit(robot, CW*.70, CH*.60); bg.alpha_composite(r, ((CW-r.width)//2, int(CH*.70)-r.height))
        c = fit(car34, CW*.92, CH*.34); bg = _ombre(bg, int(CH*.81), int(c.width*.8)); bg.alpha_composite(c, ((CW-c.width)//2, int(CH*.81)-c.height))
    else:
        c = fit(car34, CW*.96, CH*.46); bg = _ombre(bg, int(CH*.70), int(c.width*.8)); bg.alpha_composite(c, ((CW-c.width)//2, int(CH*.70)-c.height))
    return bg.convert('RGB')
