# Adding a New Op-ed
Similar to adding a new Working Paper, adding a new Op-ed requires copying the Op-ed template and filling in the Page Properties. 

However, since the page redirects users directly to the Op-ed article, there's no need to fill out the content on the page itself (i.e. authors, link, embed, etc.)


## Copy Op-ed template
In AEM, navigate to the Publications & Multimedia page and copy the Op-ed template.

1. Go to the [Publications & Multimedia page in AEM's WMC :material-arrow-top-right:](https://author.sfu.ca/siteadmin#/content/sfu/politics/CERG/works){target="_blank"}
1. Right click on the `Op-ed Template (2026)` and select `Copy`.]
1. Click `Paste` to paste the template. Change the `Copy name` to this structure: `op-ed-xx-short-title` where `xx` is the number of the Op-ed and `short-title` is a 3-6 word keywords of the title (e.g., `op-ed-10-gemany-canada-lng-purchase`).
1. The new page will show up at the end of the list of pages. You may have to go to the next page to see it.

## Fill in Page Properties
Here we add the following information into the Page Properties of the new Op-ed page:

Content to be added | Type of content | Where it goes
--------------------|-----------------|----------------
Title | The first portion of the Op-ed title, before the colon (if applicable) | `Basic -> Title`
Tags | The keywords associated with the Op-ed | `Basic -> Tags/Keywords`
Date | The date the Op-ed was published (both short `09/13/2026` and long formats `September 13, 2026`) | `Basic -> Date` and `Advanced -> Custom Properties -> custom-publication-date`
Subtitle (if applicable) | The second portion of the Op-ed title, after the colon (if applicable) | `Basic -> More Titles and Description -> Subtitle`
Overview | A brief layman's summary of the Op-ed's content (max. 50 words) | `Basic -> More Titles and Description -> Description`
Op-ed URL | The URL link to the Op-ed | `Advanced -> Redirect`
Publication Type & Number | The type (Op-ed) and number assigned to the Op-ed | `Advanced -> Custom Properties -> custom-publication-type`
Image (if applicable) | The cover image of the Op-ed as a `3:2 (Carousel)` aspect ratio | `Image`

1. Open up the page.
1. Select `Page Properties` from the `Page` menu.
1. Go through the three tabs in the Page Properties dialog and fill in the information above. If you don't have a cover image, you can leave the image field blank.

Filling in this information in Page Properties will automatically populate the Op-ed page with that information.

### Adding Tags
Tags are used to filter Op-eds by topic on the Publications & Multimedia page and Agrivoltaics page and to connect news items.

You must include the following tags for the Op-ed **in the following order** to appear in the correct places:

Type of tag | Why | Tag Name
--------------------|-----------------|----------------
Topic | To identify the topic of the Working Paper | See a [list of topics here](applying-a-working-paper-template.md#choose-a-template).
Publication Number | The number assigned to the Op-ed | X <br> where `X` is the number of the Op-ed (e.g. `21`)
Publication Medium | To identify it as a Op-ed; already on the template | Op-ed <br> `op_ed`


!!! warning "Topic tag must come first"
    Due to AEM restrictions, the topic tag must be the first tag in the list. If it is not, the Op-ed will not show the topic throughout the site.

<video controls width="100%">
  <source src="../video/adding tags to an op-ed.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
/// caption
Filling in Page Properties for an op-ed [coming soon]
///


## Activate
If everything looks good and the op-ed is ready to be added to the site, [Activate the page](../general/update-info-on-a-page.md#while-editing-inside-a-page) to save your changes and publish it.