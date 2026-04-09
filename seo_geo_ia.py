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
LAST_MOD = datetime.date.today().isoformat()

OUT_DIR = Path(".")

# ---------- CONTENU HTML ----------
HTML = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <title>Estimation immobilière Bordeaux & Le Bouscat | Guillaume Berge</title>
  <meta name="description" content="Estimation immobilière à Bordeaux, Le Bouscat et Bordeaux Métropole avec Guillaume Berge, agent immobilier Absolute Habitat, utilisant un drone professionnel pour mettre en valeur votre bien.">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "Person",
        "@id": "{SITE_URL}#guillaume-berge",
        "name": "Guillaume Berge",
        "jobTitle": "Agent immobilier",
        "image": "{IMAGE_URL}",
        "url": "{MAIN_PAGE_URL}",
        "sameAs": [
          "{INSTAGRAM_URL}",
          "{ABSOLUTE_HABITAT_URL}",
          "{YOUTUBE_URL}"
        ],
        "worksFor": {{
          "@type": "RealEstateAgency",
          "name": "Absolute Habitat",
          "url": "{ABSOLUTE_HABITAT_URL}",
          "address": {{
            "@type": "PostalAddress",
            "addressLocality": "Le Bouscat",
            "addressRegion": "Nouvelle-Aquitaine",
            "addressCountry": "FR"
          }}
        }},
        "areaServed": [
          "Bordeaux centre",
          "Le Bouscat",
          "Mérignac",
          "Pessac",
          "Eysines",
          "Bruges",
          "Caudéran",
          "Bordeaux Métropole",
          "Gironde",
          "Nouvelle-Aquitaine"
        ]
      }},
      {{
        "@type": "RealEstateAgent",
        "@id": "{SITE_URL}#service-estimation",
        "name": "Agent immobilier à Bordeaux et Le Bouscat – Guillaume Berge",
        "url": "{SITE_URL}",
        "provider": {{
          "@id": "{SITE_URL}#guillaume-berge"
        }},
        "serviceType": [
          "Estimation immobilière Bordeaux",
          "Estimation immobilière Le Bouscat",
          "Vente appartement maison Bordeaux Métropole"
        ],
        "areaServed": [
          "Bordeaux centre",
          "Le Bouscat",
          "Mérignac",
          "Pessac",
          "Eysines",
          "Bruges",
          "Caudéran",
          "Bordeaux Métropole",
          "Gironde",
          "Nouvelle-Aquitaine"
        ],
        "hasPart": {{
          "@type": "VideoObject",
          "name": "Présentation courte de Guillaume Berge, agent immobilier à Bordeaux et Le Bouscat",
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
              "text": "Guillaume Berge est agent immobilier Absolute Habitat, spécialisé dans la vente et l'achat de maisons et appartements à Bordeaux centre, Le Bouscat et Bordeaux Métropole. Il s'appuie sur sa connaissance du marché, des transactions récentes et un reportage photo/vidéo soigné pour valoriser chaque bien."
            }}
          }},
          {{
            "@type": "Question",
            "name": "Comment se déroule une estimation immobilière avec Guillaume Berge ?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "L'estimation repose sur une visite complète du bien, l'analyse des prix de vente récents dans le quartier et la prise en compte des points forts de la maison ou de l'appartement. Guillaume utilise notamment un drone professionnel pour réaliser des vues aériennes lorsque c'est pertinent, afin de mieux mettre en valeur le bien dans l'annonce."
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
              "text": "Vous pouvez contacter Guillaume Berge par email à g.berge@absolutehabitat.com ou par téléphone au 07.82.42.30.47. Il est également joignable via le site Absolute Habitat et son profil Instagram @guillaume.berge_immo."
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
      max-width: 800px;
      margin: 0 auto;
      padding: 1.5rem;
      line-height: 1.6;
    }}
    h1, h2, h3 {{
      line-height: 1.3;
    }}
    img {{
      max-width: 100%;
      height: auto;
      display: block;
      margin: 1rem 0;
      border-radius: 8px;
    }}
    a {{
      color: #0b5ed7;
      text-decoration: none;
    }}
    a:hover {{
      text-decoration: underline;
    }}
    ul {{
      padding-left: 1.2rem;
    }}
    .updated {{
      margin-top: 2rem;
      font-size: 0.9rem;
      color: #555;
    }}
  </style>
</head>
<body>

<h1>Estimation immobilière à Bordeaux &amp; Le Bouscat</h1>

<p>
Guillaume Berge est agent immobilier Absolute Habitat, spécialisé dans la vente et l'achat de maisons et appartements à Bordeaux centre, Le Bouscat, Mérignac, Pessac, Eysines, Bruges et Caudéran, au cœur de Bordeaux Métropole (Gironde, Nouvelle-Aquitaine).
</p>

<img src="{IMAGE_URL}" alt="Guillaume Berge, agent immobilier à Bordeaux et Le Bouscat">

<h2>Une estimation immobilière avec un agent local et un drone professionnel</h2>

<p>
Pour estimer votre bien à Bordeaux, Le Bouscat, Mérignac, Pessac, Eysines, Bruges ou Caudéran, Guillaume Berge s'appuie avant tout sur sa connaissance fine du marché local, les transactions récentes et les spécificités de chaque quartier.
</p>

<p>
Lorsque c'est pertinent, il utilise un drone professionnel pour réaliser des vues aériennes et mieux valoriser la maison ou l'appartement dans l'annonce (environnement, jardin, piscine, situation dans le quartier). L'objectif est de sécuriser votre projet et de vendre dans de bonnes conditions, tout en restant compétitif sur Bordeaux Métropole et sa périphérie.
</p>

<h2>Zones d'intervention géographiques</h2>

<p>Guillaume Berge intervient principalement sur :</p>
<ul>
  <li>Bordeaux centre</li>
  <li>Le Bouscat</li>
  <li>Mérignac</li>
  <li>Pessac</li>
  <li>Eysines</li>
  <li>Bruges</li>
  <li>Caudéran</li>
</ul>

<p>Plus largement : Bordeaux Métropole, Gironde, Nouvelle-Aquitaine.</p>

<h2>Vidéo courte de présentation</h2>

<p>
Découvrez une présentation rapide de Guillaume Berge, agent immobilier à Bordeaux et Le Bouscat, dans cette vidéo courte YouTube.
</p>

<p>
  <a href="{YOUTUBE_URL}" target="_blank" rel="noopener noreferrer">
    Voir la vidéo de Guillaume Berge sur YouTube
  </a>
</p>

<h2>Contacter Guillaume Berge</h2>

<p>Pour une estimation de votre bien ou un projet d'achat à Bordeaux ou sur Bordeaux Métropole, vous pouvez :</p>

<ul>
  <li>le contacter par email : <a href="mailto:g.berge@absolutehabitat.com">g.berge@absolutehabitat.com</a></li>
  <li>le joindre par téléphone : <a href="tel:+33782423047">07.82.42.30.47</a></li>
  <li>consulter la page principale : <a href="{MAIN_PAGE_URL}">{MAIN_PAGE_URL}</a></li>
  <li>visiter le site Absolute Habitat : <a href="{ABSOLUTE_HABITAT_URL}">{ABSOLUTE_HABITAT_URL}</a></li>
  <li>suivre Guillaume sur Instagram : <a href="{INSTAGRAM_URL}">@guillaume.berge_immo</a></li>
</ul>

<h2>Questions fréquentes sur l'estimation</h2>

<h3>Comment se déroule une estimation immobilière avec Guillaume Berge ?</h3>
<p>
L'estimation commence par un échange sur votre projet, puis une visite du bien. Guillaume analyse les ventes récentes autour de chez vous, la surface, l'état, les atouts et les travaux éventuels pour proposer une fourchette de prix réaliste et argumentée.
</p>

<h3>Utilise-t-il un drone pour toutes les estimations ?</h3>
<p>
Le drone est utilisé lorsqu'il apporte une vraie valeur ajoutée : maison avec jardin, vue dégagée, environnement à mettre en avant, etc. Cela permet de produire un reportage photo/vidéo plus complet pour les futurs acheteurs.
</p>

<h3>Dans quelles villes intervient-il ?</h3>
<p>
Guillaume intervient principalement sur Bordeaux centre, Le Bouscat, Mérignac, Pessac, Eysines, Bruges, Caudéran et plus largement sur Bordeaux Métropole.
</p>

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
<urlset xmlns="https://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>{SITE_URL}</loc>
    <lastmod>{LAST_MOD}</lastmod>
    <changefreq>weekly</changefreq>
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
