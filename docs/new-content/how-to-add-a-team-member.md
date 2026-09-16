# Creating a team member

??? info "Prerequisites"
    You must be signed into your SFU account and have access to AEM in order to make changes. If you do not have access, please [contact Andy](mailto:ahira@sfu.ca) to request access.

    Have these details for the team member ready to fill in the page:

     - Name
     - What they do (i.e. Political Science professor @ SFU)
     - Bio (paragraph or two about their work/research)
     - Contact Information (i.e. LinkedIn profile, email)
     - Headshot photo (square, 1:1 ratio, at least 500px x 500px)


## Copy the template
In AEM, navigate to the CERG Team page and copy the Team Member Template.

[CERG Team page in AEM's WMC :material-arrow-top-right-thick:](https://author.sfu.ca/siteadmin#/content/sfu/politics/cerg/cerg-team){.md-button .md-button--primary target="_blank"}

1. In the events page, right click on the `Team Member Template` and select `Copy`.
1. Click `Paste` to paste the template. Change the `Copy name` to this structure: `firstname-lastname` where:
    - `firstname` is the team member's first name
    - `lastname` is the team member's last name (if applicable)
1. The new page will show up at the end of the list of pages. You may have to go to the next page to see it.


## Fill in Page Properties
Here we add the following information into the Page Properties of the new team member page:

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
1. Go through the `Basic`, `Advanced`, and `Image` tabs in the Page Properties dialog and fill in the information above.

Filling in this information in Page Properties will automatically populate the team member page with that information.


## Fill in the page
While most content is added through Page Properties, some content is added directly to the page. This includes:

Content to be added | Type of content | Where it goes
--------------------|-----------------|----------------
Team Member Bio | A paragraph or two about their work/research | On right side of the page
Contact Information | Include at least one contact detail (LinkedIn, email) | In red box on left side of the page

### Add the team member bio
Simply edit the About text box on the right side of the page to add a brief bio about the team member. This should be a short paragraph that describes their work, research, and contributions related to the field.

<video controls width="100%">
  <source src="../video/how to change the event summary.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
/// caption
Editing the event summary
///



### Add their contact information
Simply edit the red box on the left side of the page to add at least one contact detail for the team member. This can be a LinkedIn profile, email address, or any other relevant contact information.

To be consistent, add the contact information in the following bulleted format:


- LinkedIn: [https://www.linkedin.com/in/mnielsen-/](https://www.linkedin.com/in/mnielsen-/)
- Email: [mhn8@sfu.ca](mailto:mhn8@sfu.ca)
- Phone: 778-636-4131

Remember to add hyperlinks where appropriate (e.g., LinkedIn profile, email address) so that users can easily click to connect with the team member.

<video controls width="100%">
  <source src="../video/adding related working paper to event page.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
/// caption
Setting the related working paper
///


## Change order of team members
The order of the team member pages in AEM will reflect the order they appear on the CERG Team page.

To change that order, drag and drop the team member page to the desired position in the list of other team member pages. 

<video controls width="100%">
  <source src="../video/adding related working paper to event page.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
/// caption
Changing the order of team members
///


## Activate
If everything looks good and the event is ready to be added to the site, [Activate the page](../general/update-info-on-a-page.md#while-editing-inside-a-page) to save your changes and publish it.