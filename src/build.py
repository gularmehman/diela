from pathlib import Path
root=Path(__file__).resolve().parent.parent
s=(root/'src/diela-editorial.html').read_text()
for token,file in {'HERO_AM':'hero-am','HERO_PM':'hero-pm','SHELF_CURATED':'shelf-curated','CHECKIN':'checkin-am','ROUTINE_GRID':'routine-curated','TODAY_AM':'today-am'}.items():s=s.replace('{{'+token+'}}',(root/'src/native'/f'{file}.html').read_text())
assert '{{' not in s
(root/'dist/index.html').write_text(s)
(root/'dist/diela.css').write_text((root/'src/editorial.css').read_text()+'\n'+(root/'src/dawn.css').read_text())
(root/'dist/interaction.js').write_text((root/'src/editorial.js').read_text())
print('Built Diela editorial direction with native interface excerpts.')
