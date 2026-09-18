# Creating an event
??? info "Prerequisites"

    Have as much of the details for the event ready as possible to fill in the page:

    - Title
    - Summary
    - Date
    - Time
    - Location
    - EventBrite link


## Creating multiple ticket types in EventBrite

<div class="grid" markdown>

  Watch this video to learn how to create an event that has both in-perosn and online attendance options:
 
<video controls width="100%">
  <source src="../video/multiple ticket types in eventbrite.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
/// caption
Multiple Ticket Types in EventBrite
///

</div>



## Copy the event template
In AEM, navigate to the events page and copy the event template.

[Events page in AEM's WMC :material-arrow-top-right-thick:](https://author.sfu.ca/siteadmin#/content/sfu/politics/CERG/events){.md-button .md-button--primary target="_blank"}

1. In the events page, right click on the `202X Event Template` and select `Copy`.
1. Click `Paste` to paste the template. Change the `Copy name` to this structure: `202X-XX-short-title` where:
    - `X` is the year
    - `XX` is the month
    - `short-title` is 3-6 keywords of the event title (e.g., `2027-01-alternative-energy-comparison`).
1. The new page will show up at the end of the list of pages. You may have to go to the next page to see it.


## Fill in Page Properties
Here we add the following information into the Page Properties of the new event page:

Content to be added | Type of content | Where it goes
--------------------|-----------------|----------------
Title | The first portion of the event title, before the colon (if applicable) | `Basic -> Title`
Tags | The keywords associated with the event | `Basic -> Tags/Keywords`
Date | The date the event is scheduled (both short `09/13/2026` and long formats `September 13, 2026`) | `Basic -> Date` and `Advanced -> Custom Properties -> custom-event-date`
Subtitle (if applicable) | The second portion of the event title, after the colon (if applicable) | `Basic -> More Titles and Description -> Subtitle`
Event Location | A simple description of the event location (e.g., `SFU Burnaby Campus; AQ 1000`) | `Advanced -> Custom Properties -> custom-event-location-simple`
Location Type | The type of the event location (e.g., `Online`, `In-person`, `Hybrid`) | `Advanced -> Custom Properties -> custom-event-location-type`
Event RSVP Link | The URL link to the event registration page | `Advanced -> Custom Properties -> custom-event-rsvp-link`
Event Time | The time the event is scheduled | `Advanced -> Custom Properties -> custom-event-time`

1. Open up the page.
1. Select `Page Properties` from the `Page` menu.
1. Go through the `Basic` and `Advanced` tabs in the Page Properties dialog and fill in the information above.

Filling in this information in Page Properties will automatically populate the event page with that information.

### Adding Tags
Tags are used to filter events by topic on the Publications & Multimedia page and Agrivoltaics page.

You must include the following tags for the event **in the following order** to appear in the correct places:

Type of tag | Why | Tag Name
--------------------|-----------------|----------------
Topic | To identify the topic of the Working Paper | See a [list of topics here](applying-a-working-paper-template.md#choose-a-template).
Event | To identify it as an event; already on the template | Event <br> `event`

<video controls width="100%">
  <source src="../video/adding tags to an op-ed.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
/// caption
Filling in Page Properties for an event [coming soon]
///


## Editing the event page
While most content is added through Page Properties, some content is added directly to the page. This includes:

Content to be added | Type of content | Where it goes
--------------------|-----------------|----------------
Summary | A brief overview of the event | On right side of the page
Related works | optional; links to the related working paper | Below summary

### Add the event summary
Simply edit the summary text box on the right side of the page to add a brief overview of the event. This should be a short paragraph that describes the event and what's being presented, includes sponsors and collaborators, and entices users to register.

<video controls width="100%">
  <source src="../video/how to change the event summary.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
/// caption
Editing the event summary
///



### Add the related working paper (optional)
If the event is presenting a working paper, and you have the working paper [already created in AEM](adding-a-working-paper.md), you can set this section to display the working paper card on the event page.

**If your event doesn't have one or you don't want to display it, delete this component and it's header.**

If you still want to add it:

1. Right click the Working Paper Tempalte (2026) card and select `Edit`.
1. Go to the `Fixed list` tab
1. Click the `Search` icon button next to the current list item and select the working paper you want to link to the event.
1. Click `OK` to save your changes and close the dialog.

<video controls width="100%">
  <source src="../video/adding related working paper to event page.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
/// caption
Setting the related working paper
///


## Activate
If everything looks good and the event is ready to be added to the site, [Activate the page](../general/update-info-on-a-page.md#while-editing-inside-a-page) to save your changes and publish it.