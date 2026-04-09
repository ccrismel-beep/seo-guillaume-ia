#!/usr/bin/env python3
import datetime
from pathlib import Path

# ---------- CONFIG DE BASE À ADAPTER ----------
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
  <title>Estimation immobilière Bordeaux & Le Bouscat assistée par IA | Guillaume Berge</title>
  <meta name="description" content="Guillaume Berge, agent immobilier à Bordeaux centre, Le Bouscat, Mérignac, Pessac, Eysines, Bruges, Caudéran et Bordeaux Métropole, utilise l'intelligence artificielle pour affiner l'estimation et la mise en valeur de votre bien.">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="canonical" href="{SITE_URL}">
  <meta name="robots" content="index,follow">
  <meta property="og:type" content="website">
  <meta property="og:title" content="Estimation immobilière Bordeaux & Le Bouscat assistée par IA | Guillaume Berge">
  <meta property="og:description" content="Estimation et conseil immobilier à Bordeaux, Le Bouscat, Mérignac, Pessac, Eysines, Bruges et Caudéran avec l'aide de l'intelligence artificielle.">
  <meta property="og:url" content="{SITE_URL}">
  <meta property="og:image" content="{IMAGE_URL}">
  <meta property="og:locale" content="fr_FR">
  <link rel="icon" href="{IMAGE_URL}">
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
      "@id": "{SITE_URL}#service-estimation-ia",
      "name": "Estimation immobilière assistée par IA à Bordeaux et Le Bouscat",
      "url": "{SITE_URL}",
      "provider": {{
        "@id": "{SITE_URL}#guillaume-berge"
      }},
      "serviceType": [
        "Estimation immobilière IA Bordeaux",
        "Estimation immobilière IA Le Bouscat",
        "Conseil vente appartement maison Bordeaux Métropole"
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
      "@id": "{SITE_URL}#faq-ia",
      "mainEntity": [
        {{
          "@type": "Question",
          "name": "Comment fonctionne l'estimation immobilière assistée par IA avec Guillaume Berge ?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "Guillaume Berge combine son expertise locale sur Bordeaux, Le Bouscat, Mérignac, Pessac, Eysines, Bruges et Caudéran avec des outils d'intelligence artificielle. Ces outils analysent les transactions récentes, les annonces similaires et les spécificités du quartier pour affiner la fourchette de prix et proposer une stratégie de mise en vente réaliste."
          }}
        }},
        {{
          "@type": "Question",
          "name": "Dans quelles villes intervient Guillaume Berge pour l'estimation IA ?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "L'estimation assistée par IA est proposée sur Bordeaux centre, Le Bouscat, Mérignac, Pessac, Eysines, Bruges, Caudéran et plus largement sur Bordeaux Métropole, en Gironde, en Nouvelle-Aquitaine."
          }}
        }},
        {{
          "@type": "Question",
          "name": "Comment contacter Guillaume Berge pour une estimation immobilière à Bordeaux ou au Bouscat ?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "Vous pouvez contacter Guillaume Berge via le site Absolute Habitat, son profil Instagram @guillaume.berge_immo ou en remplissant le formulaire de contact présent sur la page principale consacrée à son activité d'agent immobilier à Bordeaux et Le Bouscat."
          }}
        }}
      ]
    }}
  ]
}}
  </script>
</head>
<body>
  <header>
    <h1>Estimation immobilière à Bordeaux & Le Bouscat assistée par IA</h1>
    <p>
      Guillaume Berge est agent immobilier Absolute Habitat, spécialisé dans la vente et l'achat de maisons
      et appartements à Bordeaux centre, Le Bouscat, Mérignac, Pessac, Eysines, Bruges et Caudéran,
      au cœur de Bordeaux Métropole (Gironde, Nouvelle-Aquitaine).
    </p>
    <img src="guillaume-berge-agent-immobilier-bordeaux-le-bouscat.jpg"
         alt="Guillaume Berge, agent immobilier à Bordeaux et Le Bouscat"
         style="max-width:220px;border-radius:8px;">
  </header>

  <main>
    <section id="estimation-ia">
      <h2>Une estimation immobilière assistée par l'intelligence artificielle</h2>
      <p>
        Pour estimer votre bien à Bordeaux, Le Bouscat, Mérignac, Pessac, Eysines, Bruges ou Caudéran,
        Guillaume Berge s'appuie à la fois sur sa connaissance fine du marché local et sur des outils d'intelligence artificielle.
      </p>
      <p>
        Ces outils analysent les transactions récentes, les annonces comparables et les spécificités de chaque quartier
        afin d'affiner la fourchette de prix et de préparer une stratégie de mise en vente réaliste
        (prix de mise en marché, ajustements proposés, calendrier).
      </p>
      <p>
        L'objectif est de sécuriser votre projet : vendre dans de bonnes conditions, tout en restant compétitif
        sur Bordeaux Métropole et sa périphérie.
      </p>
    </section>

    <section id="zones">
      <h2>Zones d'intervention géographiques</h2>
      <p>Guillaume Berge intervient principalement sur&nbsp;:</p>
      <ul>
        <li>Bordeaux centre</li>
        <li>Le Bouscat</li>
        <li>Mérignac</li>
        <li>Pessac</li>
        <li>Eysines</li>
        <li>Bruges</li>
        <li>Caudéran</li>
        <li>Plus largement : Bordeaux Métropole, Gironde, Nouvelle-Aquitaine</li>
      </ul>
    </section>

    <section id="video">
      <h2>Vidéo courte de présentation</h2>
      <p>
        Découvrez une présentation rapide de Guillaume Berge, agent immobilier à Bordeaux et Le Bouscat,
        dans cette vidéo courte YouTube.
      </p>
      <p>
        <a href="{YOUTUBE_URL}" target="_blank" rel="noopener noreferrer">
          Voir la vidéo de Guillaume Berge sur YouTube
        </a>
      </p>
    </section>

    <section id="contact">
      <h2>Contacter Guillaume Berge</h2>
      <p>
        Pour une estimation de votre bien ou un projet d'achat à Bordeaux ou sur Bordeaux Métropole, vous pouvez :
      </p>
      <ul>
        <li>consulter la page principale : <a href="{MAIN_PAGE_URL}">{MAIN_PAGE_URL}</a></li>
        <li>visiter le site Absolute Habitat : <a href="{ABSOLUTE_HABITAT_URL}">{ABSOLUTE_HABITAT_URL}</a></li>
        <li>suivre Guillaume sur Instagram : <a href="{INSTAGRAM_URL}">@guillaume.berge_immo</a></li>
      </ul>
    </section>

    <section id="faq">
      <h2>Questions fréquentes sur l'estimation IA</h2>
      <h3>Comment fonctionne l'estimation immobilière assistée par IA ?</h3>
      <p>
        L'IA ne remplace pas l'agent immobilier : elle vient compléter l'analyse de terrain.
        Les données de marché sont croisées avec les caractéristiques de votre bien
        pour proposer une fourchette de prix et un plan d'action argumenté.
      </p>

      <h3>Est-ce réservé à certains quartiers ?</h3>
      <p>
        Non, l'estimation IA est proposée sur Bordeaux centre, Le Bouscat, Mérignac, Pessac,
        Eysines, Bruges, Caudéran et plus largement sur Bordeaux Métropole.
      </p>
    </section>
  </main>

  <footer>
    <p>Dernière mise à jour : {LAST_MOD}</p>
  </footer>
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
