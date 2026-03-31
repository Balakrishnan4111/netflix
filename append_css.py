import os
base_dir = r"c:/Users/acer/Desktop/frontend/projects html and css"

appends = {
    "index.css": """
/* === RESPONSIVE OVERRIDES (Do not edit existing code) === */
@media (max-width: 768px) {
    .container { height: auto; min-height: 100vh; }
    nav { flex-direction: column; height: auto; padding: 20px; align-items: center; }
    .in { margin-left: 0; margin-top: 10px; width: 100%; max-width: 200px; }
    select { position: static; margin: 10px 0; left: 0; }
    .middle { margin: 20px; text-align: center; }
    h1 { font-size: 28px; }
    input { width: 100%; top: 0; }
    .get { width: 100%; top: 0; margin-top: 10px; }
    .container1 { height: auto; min-height: 100vh; padding: 20px 0; }
    .content { grid-template-columns: repeat(2, 1fr); justify-items: center; }
    .card1, .card2, .card3, .card4, .card5, .card6, .card7, .card8 { margin-left: 0; width: 100%; max-width: 140px; }
    .and { left: 0; font-size: 24px; top: 0; }
    .content1 { grid-template-columns: 1fr; }
    .card9, .card10, .card11, .card12 { width: 90%; margin: 20px auto; padding: 20px; height: auto; }
    .join { margin-left: 0; text-align: center; }
    .smart, .en { margin-left: 0; text-align: center; }
    .box { width: 90%; flex-direction: column; height: auto; padding: 20px; align-items: flex-start; margin: 20px auto; }
    .ask { margin-left: 0; }
    .foot { width: 100%; max-width: 454px; }
    .start { width: 100%; max-width: 180px; }
    .footer2 { grid-template-columns: 1fr; margin-left: 20px; text-align: left; }
    .lan { margin-left: 0; margin-top: 10px; }
    .last, .india { margin-left: 0; text-align: left; }
}
""",
    "signin.css": """
/* === RESPONSIVE OVERRIDES === */
@media (max-width: 768px) {
    h1 { width: 100%; max-width: 440px; font-size: 24px; padding: 0 20px; margin-top: 20px; }
    input { width: 90%; max-width: 440px; }
    button { width: 90%; max-width: 440px; }
    select { position: static; margin-left: 0; top: 0; margin-top: 20px; display: block; }
    p { display: block; padding: 10px 20px; margin-left: 0; }
    .container1 { height: auto; padding: 20px; }
    .end { height: auto; }
    .first, .second { flex-direction: column; align-items: flex-start; padding: 10px 20px; gap: 10px; }
    a { margin-top: 10px; padding: 0; }
    .call { position: static; left: 0; padding: 10px 20px; }
}
""",
    "FAQ.css": """
/* === RESPONSIVE OVERRIDES === */
@media (max-width: 768px) {
    .container { height: auto; min-height: 100vh; }
    nav { height: auto; flex-direction: column; padding: 20px; align-items: center; }
    img { margin-left: 0; }
    .btn { flex-wrap: wrap; margin-top: 10px; }
    .btn2 { margin-top: 0; }
    h1 { font-size: 28px; margin-left: 10px; }
    .card { position: static; left: 0; top: 0; width: 90%; margin: 20px auto; }
    .first, .second, .third, .fourth, .Fifth { width: 90%; height: auto; aspect-ratio: 16/9; margin-left: auto; margin-right: auto; }
    hr { width: 90%; margin-left: 5%; }
    .container1 { height: auto; padding-bottom: 30px; }
    select { margin-left: auto; margin-right: auto; display: block; }
    .lan { margin-left: 0; }
    .footer { padding: 0 20px; }
    ol { margin-left: 10px; }
}
""",
    "contact.css": """
/* === RESPONSIVE OVERRIDES === */
@media (max-width: 768px) {
    nav { height: auto; flex-direction: column; padding: 20px; gap: 10px; }
    .btn1, .btn2 { margin-left: 0; left: 0; }
    .content { margin-left: 0; padding: 0 20px; }
    h1 { font-size: 28px; }
    input { width: 100%; max-width: 665px; }
    hr { width: 100%; }
    .container1 { height: auto; padding: 40px 20px; }
    select { position: static; left: 0; margin-top: 0; margin-bottom: 20px; }
    .footer { flex-direction: column; }
    .a7, .a8, .a9, .a10 { margin-left: 0; left: 0; top: 0; margin: 10px 0; }
}
"""
}

for filename, content in appends.items():
    with open(os.path.join(base_dir, filename), "a", encoding="utf-8") as f:
        f.write(content)
print("Done appending CSS!")
