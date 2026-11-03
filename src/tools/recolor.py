"""Recoloration par code d'une base « rouge » : seuls les pixels rouges changent (teinte, saturation, luminosité).
Le noir, le crème, le gris et les contours restent identiques. Fond vert retiré automatiquement.
Usage : python src/tools/recolor.py image.png [dossier_sortie]  -> une image par couleur + une planche de démo."""
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage as ndi
from matplotlib.colors import rgb_to_hsv, hsv_to_rgb

def key(path):
    a=np.asarray(Image.open(path).convert('RGB')).astype(float)
    r,g,b=a[...,0],a[...,1],a[...,2]
    green=g-np.maximum(r,b)               # >0 : pixel "vert"
    alpha=np.clip(1-(green-30)/110,0,1)   # fond vert -> transparent, bords adoucis
    # désaturer le liseré vert des bords
    rgb=a.copy(); spill=np.clip(green,0,None)*(alpha>0)
    rgb[...,1]=np.minimum(g,np.maximum(r,b)+np.where(alpha<1,0,0))
    im=np.dstack([np.clip(rgb,0,255),alpha*255]).astype(np.uint8)
    return Image.fromarray(im,'RGBA')
def frames(im,n):
    al=np.asarray(im)[...,3]>40
    al=ndi.binary_closing(al,iterations=6);lab,k=ndi.label(al);sl=ndi.find_objects(lab)
    sz=ndi.sum(al,lab,range(1,k+1));keep=[sl[i] for i in range(k) if sz[i]>0.003*al.size]
    keep=sorted(keep,key=lambda s:s[1].start)[:n]
    return [im.crop((s[1].start,s[0].start,s[1].stop,s[0].stop)) for s in keep]
def base_hue(imgs):
    """Teinte dominante (0 à 1) des pixels bien colorés d'une ou plusieurs images : c'est la « couleur de base » à remplacer."""
    H=[]
    for im in imgs:
        a=np.asarray(im.convert('RGBA')).astype(float);hsv=rgb_to_hsv(a[...,:3]/255);m=(a[...,3]>200)&(hsv[...,1]>.5)&(hsv[...,2]>.35)
        H.append(np.repeat(hsv[...,0][m],1))
    h=np.concatenate(H) if H else np.array([0.]);hist=np.bincount((h*100).astype(int)%100,minlength=100).astype(float)
    hist=np.convolve(np.r_[hist[-3:],hist,hist[:3]],np.ones(5)/5,'same')[3:-3];return (np.argmax(hist)+.5)/100
def recolor(im,hue,sat=1.0,vmul=1.0,vadd=0.0,grey=False,base=0.0):
    """Recolore les pixels de teinte « base » (± 0,07) : nouvelle teinte, saturation x sat, luminosité x vmul + vadd."""
    a=np.asarray(im).astype(float);rgb=a[...,:3]/255;al=a[...,3]
    hsv=rgb_to_hsv(rgb);h,s,v=hsv[...,0],hsv[...,1],hsv[...,2]
    d=np.abs(h-base);d=np.minimum(d,1-d)
    red=(d<.07)&(s>0.35)&(v>0.25)
    nh=np.where(red,hue,h);ns=np.where(red,np.clip(s*sat,0,1),s);nv=np.where(red,np.clip(v*vmul+vadd,0,1),v)
    out=hsv_to_rgb(np.dstack([nh,ns,nv]))
    res=np.where(red[...,None],out,rgb)
    return Image.fromarray(np.dstack([res*255,al]).astype(np.uint8),'RGBA')
COUL=[('Rouge (original)',None),
('Bleu',(215/360,1,1,0)),('Turquoise',(180/360,1,1,0)),('Vert',(125/360,1,.95,0)),
('Jaune',(50/360,1,1.05,0)),('Orange',(24/360,1,1.05,0)),('Violet',(272/360,.95,.95,0)),
('Rose',(328/360,.65,1.1,0)),('Blanc',(0,.04,.40,.58)),('Gris',(0,.04,.55,.12)),
('Noir',(0,.10,.38,0)),('Menthe (pastel)',(150/360,.32,.55,.45)),('Lavande (pastel)',(265/360,.30,.55,.45))]
def main():
    import sys,os
    p=sys.argv[1];out=sys.argv[2] if len(sys.argv)>2 else 'recolor_out';os.makedirs(out,exist_ok=True)
    im=key(p)
    for nm,pr in COUL[1:]:
        recolor(im,*pr).save(os.path.join(out,nm.split(' ')[0].lower()+'.png'))
    print('fait :',out)
COULEURS={n.split(' ')[0]:p for n,p in COUL if p}
COULEURS['Rouge']=(0.0,1.0,0.95,0.0)   # utile pour recolorer une base d'une autre couleur en rouge   # Bleu, Turquoise, Vert, Jaune, Orange, Violet, Rose, Blanc, Gris, Noir, Menthe, Lavande
if __name__=='__main__' and len(__import__('sys').argv)>1:
    main()
elif __name__=='__main__':
    t1=key(U+'transformation1_sprite_21.png');fr=frames(t1,6);print(len(fr),[f.size for f in fr])
    car,rob=fr[0],fr[5]
    cw,ch=470,330;cols=4;rows=(len(COUL)+cols-1)//cols
    sheet=Image.new('RGB',(cols*cw,rows*ch),(11,16,56));d=ImageDraw.Draw(sheet)
    try:F=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',22)
    except:F=None
    for i,(nm,p) in enumerate(COUL):
        x0,y0=(i%cols)*cw,(i//cols)*ch
        d.rounded_rectangle((x0+6,y0+6,x0+cw-6,y0+ch-6),14,fill=(20,28,76),outline=(42,63,107),width=2)
        for im,xx in((car,0),(rob,1)):
            c=im if p is None else recolor(im,*p)
            k=235/rob.height
            c=c.resize((max(1,round(im.width*k)),max(1,round(im.height*k))),Image.LANCZOS)
            px=x0+(30 if xx==0 else 270);py=y0+260-c.height
            sheet.paste(c,(px,py),c)
        d.text((x0+20,y0+272),nm,fill=(255,255,255),font=F)
    sheet.save('demo_recoloration.png');print(sheet.size)
