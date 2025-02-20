import pytest
from bs4 import BeautifulSoup

def load_html():
    with open("index.html", "r", encoding="utf-8") as f:
        return BeautifulSoup(f, "html.parser")

def test_html_language():Document
    soup = load_html()
    assert soup.html.has_attr("lang"), "A <html> elemnek kell legyen 'lang' attribútuma!"
    assert soup.html["lang"] == "hu", "A weblap nyelve nem magyar!"

def test_html_encoding():
    soup = load_html()
    meta = soup.find("meta", charset=True)
    assert meta is not None, "Nem található a megfelelő meta charset beállítás!"
    assert meta["charset"].lower() == "utf-8", "A karakterkódolás nem UTF-8!"

def test_title():
    soup = load_html()
    title = soup.find("title")
    assert title is not None, "A <title> elem nem található!"
    assert title.text.strip() == "Lorem", "A böngészőfül szövege nem 'Lorem'!"

def test_h1_content():
    soup = load_html()
    h1 = soup.find("h1")
    assert h1 is not None, "Az <h1> elem nem található!"
    assert h1.text.strip() == "Lorem", "Az <h1> szövege nem 'Lorem'!"

def test_paragraph_content():
    soup = load_html()
    p = soup.find("p")
    assert p is not None, "A <p> elem nem található!"
    expected_text = ("Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
                     "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. "
                     "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. "
                     "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
    assert p.text.strip() == expected_text, "A bekezdés szövege nem megfelelő!"

def test_background_image():
    soup = load_html()
    style_tag = soup.find("style")
    assert style_tag is not None, "Nem található <style> elem!"
    css = style_tag.text
    assert "background-image: url('hatter.jpg')" in css, "A háttérkép nem megfelelő!"
    assert "background-repeat: repeat-x" in css, "A háttérkép ismétlődése nem megfelelő!"
    assert "background-position: top" in css, "A háttérkép pozíciója nem megfelelő!"
    assert "background-size: 180px 180px" in css, "A háttérkép mérete nem megfelelő!"
