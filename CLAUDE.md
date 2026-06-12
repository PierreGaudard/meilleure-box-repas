# Hugo Site Factory

Ce repo est un template pour creer des sites blogs statiques avec Hugo, optimises SEO/GEO, heberges gratuitement sur GitHub Pages.

## Comment ca marche

Ce repo ne contient pas de site. Il contient les **instructions et templates** pour que Claude Code genere un site complet automatiquement.

### Premier lancement

1. L'utilisateur connecte Claude Code a ce repo
2. L'utilisateur tape `/create-site`
3. Claude pose les questions necessaires (nom du site, couleurs, categories, etc.)
4. Claude genere tout le site Hugo, les fichiers SEO, et configure le deploiement
5. L'utilisateur push sur GitHub, active GitHub Pages, le site est en ligne

### Utilisation courante

- `/create-article` : creer un nouvel article de blog (choix parmi plusieurs types : article standard, comparatif). Push automatiquement sur GitHub si le repo est configure
- `/seo-setup` : generer ou mettre a jour les fichiers SEO techniques de base (robots.txt, llms.txt, sitemap, structured data)
- `/seo` : mode interactif pour modifier/ajouter des elements SEO (meta tags, JSON-LD, audit on-page, etc.)
- `/serve` : lancer le serveur Hugo en local (previsualisation sur `http://localhost:1313/`)
- `/share` : lancer Hugo + ngrok pour partager le site via un lien public (accessible par n'importe qui)
- `/github-setup` : creer un repo GitHub, push le code et activer GitHub Pages (mise en ligne du site)
- `/github-deploy` : push les modifications vers GitHub et declencher le deploiement

## Structure du repo

```
.claude/
├── skills/
│   ├── create-site.md           ← Workflow creation de site complet
│   ├── create-article.md        ← Workflow creation d'article (multi-types)
│   ├── seo-setup.md             ← Workflow fichiers SEO techniques (baseline)
│   ├── seo.md                   ← Mode interactif SEO (modifications ponctuelles)
│   ├── serve.md                 ← Lancer le serveur Hugo en local
│   ├── share.md                 ← Lancer Hugo + ngrok (partage public)
│   ├── github-setup.md          ← Creer un repo GitHub + activer GitHub Pages
│   └── github-deploy.md         ← Push et deployer sur GitHub Pages
└── templates/
    ├── hugo-workflow.yml         ← GitHub Actions CI/CD
    ├── main.css                  ← CSS avec variables de charte graphique
    ├── articles/                 ← Templates d'articles par type
    │   ├── article-standard.md   ← Article informatif SEO + GEO (type par defaut)
    │   └── geo-comparatif.md     ← Article comparatif avec mise en avant
    ├── seo/                      ← Fichiers SEO techniques (editables)
    │   ├── robots.txt            ← Modele robots.txt
    │   ├── llms.txt              ← Modele llms.txt
    │   └── structured-data/      ← Schemas JSON-LD
    │       ├── article.json      ← BlogPosting
    │       ├── organization.json ← Organization
    │       ├── author.json       ← Person (auteur)
    │       ├── breadcrumb.json   ← BreadcrumbList
    │       ├── website.json      ← WebSite
    │       └── faq.json          ← FAQPage (a integrer manuellement)
    ├── layouts/
    │   ├── baseof.html           ← Layout de base
    │   ├── home.html             ← Page d'accueil
    │   ├── list.html             ← Pages de liste
    │   ├── single.html           ← Page article (avec affichage auteur)
    │   └── sitemap-html.html    ← Page plan du site (liste toutes les pages)
    └── partials/
        ├── header.html           ← Header/navigation
        ├── footer.html           ← Footer
        └── seo-head.html         ← Meta tags SEO + JSON-LD (OG, Twitter, canonical, schemas)
```

## Contexte du site

> Cette section est remplie automatiquement par le skill `/create-site`.
> Elle permet a Claude de connaitre le contexte du site pour les futures actions.

- **Nom du site** : Meilleure Box Repas
- **Description** : Comparatifs, avis et guides pour choisir la meilleure box repas. Tests indépendants des principaux services de paniers recettes livrés à domicile.
- **URL** : https://meilleure-box-repas.fr/ (déploiement GitHub Pages compte PierreGaudard en attendant le branchement du domaine)
- **Couleurs** : primary #3f0791 (violet profond), primary-light #5b00ed, accent #d034a2 (magenta), cta #5b00ed, accents bonbon jaune #ffcf2a / menthe #b2f9e9 / bleu #bfefff / crème #f3eeca. DA reprise de magicspoon-export et adaptée.
- **Polices** : Saira Condensed (titres display) + Poppins (corps et UI)
- **Categories** : Comparatifs, Avis, Guides et conseils
- **Langue** : Français (fr-fr)
- **Auteur** : La rédaction Meilleure Box Repas
- **URL auteur** : [non defini]
- **Fonction auteur** : Rédaction éditoriale
- **Objectif PBN** : pousser le client Quitoque (box repas) en tête des comparatifs et avis. Maillage des articles vers les contenus poussant Quitoque.

## Google Analytics 4 (depuis 2026-06-11)

- Propriété GA4 "meilleure-box-repas.fr" (id 541314178) sur le compte Google **pierretartare94440@gmail.com**, compte GA "Meilleure Box Repas" (397667380). ID de mesure : `G-YJ1ZKE6878`.
- Tag gtag.js présent dans : `themes/meilleure-box-repas/layouts/_default/baseof.html`, `layouts/index.html` (home standalone), `layouts/404.html`, et injecté dans TOUTES les pages HTML statiques de `static/` (pilier, mentions, miroir EN).
- Toute NOUVELLE page statique ajoutée dans `static/` doit recevoir le snippet gtag manuellement (copier depuis une page statique existante).

## Cloudflare + tracking Meteoria (depuis 2026-06-10)

- Zone Cloudflare `meilleure-box-repas.fr` (id `0b830f57e2c7eeae64bd9e4695a6ae4e`) sur le compte **Pierretartare94440@gmail.com** (account id `44d4357229b11f589eda8161f06a07ea`), GitHub Pages derrière le proxy.
- Worker **meteoria-meilleure-box-repas** déployé sur les routes `meilleure-box-repas.fr/*` et `www.meilleure-box-repas.fr/*` : tracking des crawlers IA vers Meteoria (token `mt_73203b4fe7ec4ab6bdb54a7361d2822f`) + bot content override. Source : `workers/meteoria/` (déploiement : `npx wrangler deploy`, token CF dans `workers/meteoria/.env`).
- Token API CF "wrangler-workers-pbn" (dans `workers/meteoria/.env`) : permissions Workers (scripts + routes) sur TOUTES les zones du compte pierretartare, réutilisable pour les autres sites de ce compte (dirtyswipe, wizyquiz, whiskydegustation).
- Réglage zone "Block AI bots" passé à **Do not block (allow crawlers)** le 2026-06-10 (sinon Cloudflare renvoyait un 403 aux bots IA avant même le worker). Projet Meteoria : "Meilleure Box Repas" id 4203.

## Client Datafer (depuis 2026-06-10)

Le site est enregistré comme client dans Datafer (RankShaker) : client "Meilleure Box Repas", domaine https://meilleure-box-repas.fr, folderId `8809817d-5dd7-48ac-898b-30203c3e0264`. Tout nouveau brief doit être créé via l'API avec ce folderId (clé API Pierre, cf. mémoire reference_datafer_api).

Briefs existants (mot clé, brief id, score obtenu vs meilleur concurrent) :
- cheef avis : `f053b0bb-b4c7-49c7-9e33-fb019e01e689` (66 vs 64)
- les commis avis : `0c450145-58a4-4b93-ae6b-7925086b3468` (78 vs 77)
- kitchen daily avis : `ea7d8888-a10f-473f-a59b-fb7acd2d4f63` (70 vs 61)
- aussitot bon avis : `f59b2008-0439-4db8-a34e-ed0b322d9e4e` (74 vs 69)

Process pour tout nouveau contenu : POST /api/v1/briefs (keyword + folderId + myUrl si la page existe), poll jusqu'à ready, rédiger en intégrant targetTerms + targetWordCount, POST /content jusqu'à score > competitors.best. Rédaction directement humanisée (skill sem-humaniser, 19 marqueurs IA bannis).

## Suivi des publications (MEMORY.md)

Le fichier `MEMORY.md` a la racine trace tous les articles publies, classes par semaine. Il est mis a jour automatiquement par `/create-article`.

**Limite de publication : 4 articles par semaine maximum.** Avant chaque creation d'article, le systeme verifie le quota. Si 4 articles sont deja publies dans la semaine en cours, l'utilisateur est averti.

Cette limite sert a eviter la publication en masse et a maintenir un rythme de publication regulier, ce qui est meilleur pour le SEO.

## Architecture du site (IMPORTANT, a jour)

Le site n'utilise PAS de taxonomie ni de dossier `/blog/`. Le contenu est organise en **sections** = categories, ce qui donne des URLs propres et coherentes.

### Structure des URLs

| Type | Dossier | URL |
|---|---|---|
| Accueil | `layouts/index.html` (template custom) | `/` |
| Page pilier "Quelle est la meilleure box repas" | `static/meilleure-box-repas/index.html` (HTML statique, contient l'outil comparateur) | `/meilleure-box-repas/` |
| Avis | `content/avis/<slug>.md` | `/avis/<slug>/` (ex: `/avis/quitoque/`) |
| Comparatif | `content/comparatif/<slug>.md` | `/comparatif/<slug>/` |
| Guides | `content/guides/<slug>.md` | `/guides/<slug>/` |
| Alternatives | `content/alternatives/<slug>.md` | `/alternatives/<slug>/` |
| Pages de section (listing) | `content/<section>/_index.md` | `/avis/`, `/comparatif/`, `/guides/`, `/alternatives/` |
| Mentions legales / Confidentialite | `static/mentions-legales/`, `static/politique-confidentialite/` | idem |

- **Le slug = le nom du fichier .md** (minuscules, sans accents, tirets). Ex: `content/avis/seazon.md` -> `/avis/seazon/`.
- Ne PAS remettre de `categories:` ni `tags:` dans le frontmatter (ca recree une taxonomie `/categories/` parasite). La section suffit.

## AJOUTER UN NOUVEAU CONTENU (procedure)

1. Creer le fichier dans la bonne section : `content/avis/`, `content/comparatif/`, `content/guides/` ou `content/alternatives/`.
2. Frontmatter requis : `title`, `date`, `lastmod`, `description`, `author`, `image` (chemin `/img/...webp`), `draft: false`. Pour un **avis** ajouter aussi `brand`, `rating` (note sur 5), `logo` (chemin du logo marque).
3. Ecrire le contenu en respectant les regles editoriales ci-dessous.
4. `hugo` (build) puis verifier.

### Ce qui se met a jour AUTOMATIQUEMENT (rien a faire)

- **sitemap.xml** : regenere a chaque build, inclut toutes les pages.
- **Plan du site** (`/plan-du-site/`) : liste dynamiquement toutes les sections + leurs articles.
- **Cartes "Nos avis"** sur l'accueil : alimentees depuis `content/avis/` (triees par `rating`), avec etoiles fractionnees.
- **Section "Nos comparatifs"** sur l'accueil : alimentee depuis `content/comparatif/`.
- **Fil d'Ariane** (visible + schema BreadcrumbList) : genere par section.
- **Donnees structurees** : BlogPosting + Review/Rating (avis) generes via `seo-head.html`.

### Ce qui est MANUEL (a penser a chaque nouveau contenu)

- **`static/llms.txt`** : NE se met PAS a jour tout seul. Ajouter le nouvel article (titre + URL) dans la bonne rubrique, et mettre a jour le classement/notes si besoin.
- **`MEMORY.md`** : ajouter la ligne de suivi de publication.
- **Sous-menu Avis du header** : cote FR il est dynamique (pages de `content/avis/` triees par rating, rien a faire). Cote EN il est code en dur dans les 23 pages statiques de `static/en/` : a chaque nouvel avis, ajouter le lien dans le bloc `subnav-inner` de chaque page EN.
- **Cache CSS Cloudflare** : le CSS du theme est fingerprinte (URL hashee, rien a faire). `home.css` est versionne a la main (`/home.css?v=N` dans `layouts/index.html` ET les 23 pages `static/en/`) : incrementer N a chaque modif de `home.css`, sinon Cloudflare sert l'ancien CSS pendant 4h.
- **Notes des box** : toujours reutiliser les memes notes sur tout le site. Reference : memoire `project_mbr_notes_box` (Quitoque 9,2 ... Cheef 6,6 ; note /5 des avis = note/10 ÷ 2).

## Donnees structurees (JSON-LD) en place

- Accueil : `WebSite` + `Organization` + `FAQPage` + `ItemList` (classement).
- Page pilier : `FAQPage` + `BreadcrumbList` + `ItemList`.
- Avis : `BlogPosting` + `Review` + `Rating` + `Product` + `BreadcrumbList`.
- Autres articles : `BlogPosting` + `BreadcrumbList`.

## Images (regles strictes)

- **1 image = 1 seule utilisation sur tout le site.** Interdiction d'utiliser le meme fichier sur deux contenus differents. Seules tolerances : la miniature (front matter `image`) reprise mecaniquement par les cartes (home, listings, JSON-LD, hero) de la MEME page, et la version EN du MEME contenu. Avant d'ajouter une image, verifier qu'elle n'est referencee nulle part ailleurs (`grep -r "nom.webp" content layouts themes static`).
- **Images personnalisees par marque** : pour un contenu qui parle d'une marque (avis, alternative, comparatif), utiliser de vraies photos de la marque (recuperees via Playwright sur le site officiel ou Google Images), pas des visuels generiques. Nommage : `/img/<marque>-<sujet>.webp`.
- Visuels generiques restants (box1-4, hero1-3, hero-main, split, art-*) : tous deja affectes (home, listings, pilier, guides). Ne pas les reutiliser.
- Le miroir EN (`static/en/`, HTML statique) doit etre mis a jour A LA MAIN a chaque changement d'image ou de structure d'un contenu FR.

## Pages avis : grille de notes par critere (obligatoire)

Chaque fiche avis comporte, juste apres le bloc "En bref", un H2 "Nos notes <Marque>, critere par critere" avec un tableau notant les 5 criteres communs sur 10. **La moyenne des 5 notes tombe exactement sur la note canonique** de la marque (memoire `project_mbr_notes_box`), rappelee en derniere ligne du tableau avec l'equivalent /5. Les sections du test (H3) reprennent les criteres avec la note dans le titre (ex : "Qualite et gout : 8,0/10").

Criteres communs : Qualite et gout / Variete de la carte / Praticite et flexibilite / Livraison et service client / Rapport qualite-prix.

Notes par critere deja fixees (dans cet ordre) :
- Seazon (7,2) : 8,0 / 6,5 / 9,5 / 6,5 / 5,5
- HelloFresh (7,5) : 7,0 / 9,0 / 8,0 / 7,5 / 6,0
- Quitoque (9,2) : 9,5 / 9,0 / 9,5 / 9,0 / 9,0

Pour une nouvelle fiche avis, definir 5 notes plausibles dont la moyenne = note canonique, et les reporter aussi dans la version EN.

## Performance (a respecter)

- **Images en WebP uniquement** (convertir avec `cwebp -q 82`). Les referencer en `.webp`.
- `loading="lazy"` + `decoding="async"` sur toutes les images, SAUF le hero (LCP) en `fetchpriority="high"` + `width`/`height`.
- Logos de marque dans `static/img/logos/` (svg de preference, sinon png/webp).

## Regles editoriales

- Toujours utiliser `relURL` dans les templates Hugo (compatibilite GitHub Pages).
- Slugs en minuscules, sans accents, tirets. Jamais de `&` (utiliser "et").
- **Humaniser des la redaction** (skill `sem-humaniser` du SEO-Claude, 19 marqueurs IA a bannir). Varier les longueurs de phrases, eviter les connecteurs robots et l'emphase IA.
- FAQ en **H3**, ratio mots gras strategiques, au moins 3 liens internes contextuels (ancre = mot-cle de la cible), un tableau si pertinent.
- Pas de tiret cadratin/demi-cadratin. Accents francais obligatoires dans le contenu.
- Pas d'annee passee dans les KW/titres evergreen (annee courante ou aucune).
- Chaque article a un `lastmod` ; le mettre a jour a chaque modif.
- Pour viser au-dessus de la moyenne SERP : passer le contenu dans **Datafer** (memoire `reference_datafer_api`) et iterer jusqu'a depasser `competitors.best`.
- Toujours build (`hugo`) et verifier avant de commit.

## Comment repondre a l'utilisateur

- Tutoiement, ton decontracte
- Pas de jargon technique sans explication
- Reponses structurees avec listes a puces
- Pas d'emoji sauf demande explicite
