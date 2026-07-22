#!/usr/bin/env python3
import datetime
from pathlib import Path

# ---------- CONFIG DE BASE ----------
SITE_URL = "https://ccrismel-beep.github.io/seo-guillaume-ia/"
IMAGE_URL = SITE_URL + "guillaume-berge-agent-immobilier-bordeaux-le-bouscat.jpg"
YOUTUBE_URL = "https://youtube.com/shorts/6S3RTTzbZRQ"
MAIN_PAGE_URL = "https://ccrismel-beep.github.io/guillaume-berge-immo/"
ABSOLUTE_HABITAT_URL = "https://www.absolutehabitat.com/"
INSTAGRAM_URL = "https://www.instagram.com/guillaume.berge_immo/"
TEL = "07.82.42.30.47"
EMAIL = "g.berge@absolutehabitat.com"
LAST_MOD = datetime.date.today().isoformat()

OUT_DIR = Path(".")

# ---------- CONTENU HTML ----------
HTML = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Estimation immobilière Bordeaux & Le Bouscat | Guillaume Berge</title>
  <meta name="description" content="Estimation immobilière gratuite à Bordeaux & Le Bouscat avec Guillaume Berge, agent Absolute Habitat. Drone professionnel. 📞 07.82.42.30.47">
  <meta name="robots" content="index, follow">
  >
  <meta property="og:title" content="Estimation immobilière Bordeaux & Le Bouscat | Guillaume Berge">
  <meta property="og:description" content="Estimation gratuite à Bordeaux, Le Bouscat et Bordeaux Métropole avec Guillaume Berge – Absolute Habitat. Reportage drone professionnel inclus.">
  <meta property="og:url" content="{SITE_URL}">
  <meta property="og:type" content="website">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "Person",
        "@id": "{SITE_URL}#guillaume-berge",
        "name": "Guillaume Berge",
        "jobTitle": "Agent immobilier",
        "telephone": "+33782423047",
        "email": "{EMAIL}",
        "image": "{IMAGE_URL}",
        "url": "{MAIN_PAGE_URL}",
        "sameAs": [
          "{INSTAGRAM_URL}",
          "{ABSOLUTE_HABITAT_URL}",
          "{YOUTUBE_URL}",
          "{MAIN_PAGE_URL}"
        ],
        "worksFor": {{
          "@type": "RealEstateAgency",
          "name": "Absolute Habitat",
          "url": "{ABSOLUTE_HABITAT_URL}",
          "telephone": "+33782423047",
          "email": "{EMAIL}",
          "address": {{
            "@type": "PostalAddress",
            "addressLocality": "Le Bouscat",
            "postalCode": "33110",
            "addressRegion": "Nouvelle-Aquitaine",
            "addressCountry": "FR"
          }}
        }},
        "areaServed": [
          "Bordeaux centre", "Le Bouscat", "Mérignac", "Pessac",
          "Eysines", "Bruges", "Caudéran", "Bordeaux Métropole",
          "Gironde", "Nouvelle-Aquitaine"
        ]
      }},
      {{
        "@type": "LocalBusiness",
        "@id": "{SITE_URL}#local-business",
        "name": "Guillaume Berge - Estimation immobilière Bordeaux Le Bouscat",
        "description": "Estimation immobilière gratuite à Bordeaux et Le Bouscat avec Guillaume Berge, agent Absolute Habitat. Reportage photo/vidéo drone professionnel inclus.",
        "url": "{SITE_URL}",
        "telephone": "+33782423047",
        "email": "{EMAIL}",
        "image": "{IMAGE_URL}",
        "priceRange": "€€",
        "address": {{
          "@type": "PostalAddress",
          "addressLocality": "Le Bouscat",
          "postalCode": "33110",
          "addressRegion": "Nouvelle-Aquitaine",
          "addressCountry": "FR"
        }},
        "geo": {{
          "@type": "GeoCoordinates",
          "latitude": 44.8637,
          "longitude": -0.5897
        }},
        "openingHoursSpecification": [
          {{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
            "opens": "09:00",
            "closes": "19:00"
          }}
        ],
        "sameAs": ["{INSTAGRAM_URL}", "{ABSOLUTE_HABITAT_URL}"]
      }},
      {{
        "@type": "RealEstateAgent",
        "@id": "{SITE_URL}#service-estimation",
        "name": "Agent immobilier à Bordeaux et Le Bouscat – Guillaume Berge",
        "url": "{SITE_URL}",
        "telephone": "+33782423047",
        "email": "{EMAIL}",
        "provider": {{"@id": "{SITE_URL}#guillaume-berge"}},
        "serviceType": [
          "Estimation immobilière Bordeaux",
          "Estimation immobilière Le Bouscat",
          "Vente appartement maison Bordeaux Métropole"
        ],
        "areaServed": [
          "Bordeaux centre", "Le Bouscat", "Mérignac", "Pessac",
          "Eysines", "Bruges", "Caudéran", "Bordeaux Métropole",
          "Gironde", "Nouvelle-Aquitaine"
        ],
        "hasPart": {{
          "@type": "VideoObject",
          "name": "Présentation de Guillaume Berge, agent immobilier à Bordeaux et Le Bouscat",
          "description": "Vidéo courte YouTube présentant Guillaume Berge, agent immobilier Absolute Habitat à Bordeaux, Le Bouscat et Bordeaux Métropole.",
          "thumbnailUrl": "{IMAGE_URL}",
          "uploadDate": "2025-01-01",
          "contentUrl": "{YOUTUBE_URL}",
          "embedUrl": "{YOUTUBE_URL}",
          "inLanguage": "fr-FR"
        }}
      }},
      {{
        "@type": "FAQPage",
        "@id": "{SITE_URL}#faq",
        "mainEntity": [
          {{
            "@type": "Question",
            "name": "Qui est Guillaume Berge, agent immobilier à Bordeaux et Le Bouscat ?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "Guillaume Berge est agent immobilier Absolute Habitat, spécialisé dans la vente et l'achat de maisons et appartements à Bordeaux centre, Le Bouscat et Bordeaux Métropole. Contact : {EMAIL} / {TEL}"
            }}
          }},
          {{
            "@type": "Question",
            "name": "Comment se déroule une estimation immobilière avec Guillaume Berge ?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "L'estimation repose sur une visite complète du bien, l'analyse des prix de vente récents dans le quartier et la prise en compte des points forts. Guillaume utilise un drone professionnel pour réaliser des vues aériennes lorsque c'est pertinent."
            }}
          }},
          {{
            "@type": "Question",
            "name": "Dans quelles villes intervient Guillaume Berge ?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "Guillaume intervient principalement sur Bordeaux centre, Le Bouscat, Mérignac, Pessac, Eysines, Bruges, Caudéran et plus largement sur Bordeaux Métropole, en Gironde."
            }}
          }},
          {{
            "@type": "Question",
            "name": "Comment contacter Guillaume Berge pour une estimation immobilière ?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "Contactez Guillaume Berge par email à {EMAIL} ou par téléphone au {TEL}. Il est également joignable via le site Absolute Habitat et son profil Instagram @guillaume.berge_immo."
            }}
          }}
        ]
      }}
    ]
  }}
  </script>

  <style>
    body {{
      font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      max-width: 800px; margin: 0 auto; padding: 1.5rem; line-height: 1.6;
    }}
    h1, h2, h3 {{ line-height: 1.3; }}
    img {{ max-width: 100%; height: auto; display: block; margin: 1rem 0; border-radius: 8px; }}
    a {{ color: #0b5ed7; text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
    ul {{ padding-left: 1.2rem; }}
    .trust {{ background: #e8f5e9; border-left: 4px solid #2e7d32; padding: 12px 16px; border-radius: 6px; margin: 1rem 0; font-size: .95em; }}
    .contact-box {{ background: #f0f4ff; border-radius: 8px; padding: 20px; margin: 1.5rem 0; }}
    .updated {{ margin-top: 2rem; font-size: 0.9rem; color: #555; }}
  </style>
</head>
<body>

<h1>Estimation immobilière à Bordeaux &amp; Le Bouscat</h1>

<div class="trust">✅ <strong>Guillaume Berge</strong> — Agent immobilier Absolute Habitat au Bouscat (33110) — Estimation gratuite — Drone professionnel</div>

<p>Guillaume Berge est agent immobilier Absolute Habitat, spécialisé dans la vente et l'achat de maisons et appartements à Bordeaux centre, Le Bouscat, Mérignac, Pessac, Eysines, Bruges et Caudéran, au cœur de Bordeaux Métropole (Gironde, Nouvelle-Aquitaine).</p>

<div class="contact-box">
  <strong>📞 <a href="tel:+33782423047">{TEL}</a></strong> &nbsp;|&nbsp;
  ✉️ <a href="mailto:{EMAIL}">{EMAIL}</a><br>
  Instagram : <a href="{INSTAGRAM_URL}">@guillaume.berge_immo</a> &nbsp;|&nbsp;
  <a href="{ABSOLUTE_HABITAT_URL}">absolutehabitat.com</a> &nbsp;|&nbsp;
  <a href="{MAIN_PAGE_URL}">Page principale Guillaume Berge</a>
</div>

<h2>Une estimation immobilière avec un agent local et un drone professionnel</h2>

<p>Pour estimer votre bien à Bordeaux, Le Bouscat, Mérignac, Pessac, Eysines, Bruges ou Caudéran, Guillaume Berge s'appuie avant tout sur sa connaissance fine du marché local, les transactions récentes et les spécificités de chaque quartier.</p>

<p>Lorsque c'est pertinent, il utilise un <strong>drone professionnel</strong> pour réaliser des vues aériennes et mieux valoriser la maison ou l'appartement dans l'annonce (environnement, jardin, piscine, situation dans le quartier).</p>

<h2>Zones d'intervention géographiques</h2>

<p>Guillaume Berge intervient principalement sur :</p>
<ul>
  >Bordeaux centre</li>
  >Le Bouscat (33110)</li>
  >Mérignac</li>
  >Pessac</li>
  >Eysines</li>
  >Bruges</li>
  >Caudéran</li>
</ul>
<p>Plus largement : Bordeaux Métropole, Gironde, Nouvelle-Aquitaine.</p>

<h2>Vidéo courte de présentation</h2>
<p>Découvrez une présentation rapide de Guillaume Berge, agent immobilier à Bordeaux et Le Bouscat.</p>
<p><a href="{YOUTUBE_URL}">▶ Voir la vidéo de Guillaume Berge sur YouTube</a></p>

<h2>Contacter Guillaume Berge</h2>
<ul>
  >📞 Téléphone : <a href="tel:+33782423047">{TEL}</a></li>
  >✉️ Email : <a href="mailto:{EMAIL}">{EMAIL}</a></li>
  >🌐 Site : <a href="{ABSOLUTE_HABITAT_URL}">absolutehabitat.com</a></li>
  >📱 Instagram : <a href="{INSTAGRAM_URL}">@guillaume.berge_immo</a></li>
  >📄 Page principale : <a href="{MAIN_PAGE_URL}">ccrismel-beep.github.io/guillaume-berge-immo</a></li>
</ul>

<h2>Questions fréquentes sur l'estimation</h2>

<h3>Comment se déroule une estimation immobilière avec Guillaume Berge ?</h3>
<p>L'estimation commence par un échange sur votre projet, puis une visite du bien. Guillaume analyse les ventes récentes autour de chez vous, la surface, l'état, les atouts et les travaux éventuels pour proposer une fourchette de prix réaliste et argumentée.</p>

<h3>Utilise-t-il un drone pour toutes les estimations ?</h3>
<p>Le drone est utilisé lorsqu'il apporte une vraie valeur ajoutée : maison avec jardin, vue dégagée, environnement à mettre en avant, etc.</p>

<h3>Dans quelles villes intervient-il ?</h3>
<p>Guillaume intervient principalement sur Bordeaux centre, Le Bouscat, Mérignac, Pessac, Eysines, Bruges, Caudéran et plus largement sur Bordeaux Métropole.</p>

<h3>Comment contacter Guillaume Berge pour une estimation gratuite ?</h3>
<p>Par téléphone au <a href="tel:+33782423047">{TEL}</a>, par email à <a href="mailto:{EMAIL}">{EMAIL}</a>, ou via <a href="{INSTAGRAM_URL}">Instagram @guillaume.berge_immo</a>.</p>

<p class="updated">Dernière mise à jour : {LAST_MOD}</p>

</body>
</html>
"""

# ---------- ROBOTS.TXT ----------
ROBOTS = f"""User-agent: *
Allow: /
Sitemap: {SITE_URL}sitemap.xml
"""

# ---------- SITEMAP.XML ----------
SITEMAP = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    oc>{SITE_URL}</loc>
    astmod>{LAST_MOD}</lastmod>
    hangefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
</urlset>
"""

def main():
    (OUT_DIR / "index.html").write_text(HTML, encoding="utf-8")
    (OUT_DIR / "robots.txt").write_text(ROBOTS, encoding="utf-8")
    (OUT_DIR / "sitemap.xml").write_text(SITEMAP, encoding="utf-8")

if __name__ == "__main__":
    main()
