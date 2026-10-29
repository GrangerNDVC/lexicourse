"""Test rapide : ouvre index.html dans un navigateur sans interface, vérifie qu'il n'y a aucune erreur et que le jeu tourne.
Prérequis : pip install playwright && playwright install chromium    Usage : python tests/smoke_test.py"""
from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT = Path(__file__).resolve().parents[1]
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width':960,'height':540}); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto((ROOT/'index.html').as_uri()); pg.wait_for_timeout(1500)
    pg.evaluate("pos=gates[0].z-9000;v=1800"); pg.wait_for_timeout(1500)
    pg.screenshot(path=str(ROOT/'tests'/'dernier_test.png'))
    fps = pg.evaluate("fps"); b.close()
assert not errs, errs; assert fps > 20, fps
print('OK : aucune erreur, %d images/s' % fps)
