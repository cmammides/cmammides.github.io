# Christos Mammides, personal website

Built with [Quarto](https://quarto.org) and published automatically to GitHub Pages.

## How to update the site

You can edit everything in the GitHub web interface. Open a file, click the pencil icon, make the change and click **Commit changes**. The site rebuilds and goes live within about two minutes. You can follow progress under the **Actions** tab.

| To change… | Edit this file |
|---|---|
| Homepage text, news, selected papers, contact | `index.qmd` |
| Research themes | `research.qmd` |
| Publication list | `publications.qmd` (copy an existing entry and paste it under the right year) |
| Grants and awards | `grants.qmd` |
| CV | `cv.qmd` |
| Menu, links, site description | `_quarto.yml` |
| Colours and fonts | `styles.scss` |

## Photos

To add a photo, upload it to the `images/` folder (**Add file → Upload files**), then reference it, e.g. `images/portrait.jpg`.
The homepage portrait and research photo are currently loaded from the old WordPress site. Upload them to `images/` and update the two links before you delete that site.

## Previewing locally (optional)

Install Quarto, open this folder in RStudio or a terminal, and run `quarto preview`.
