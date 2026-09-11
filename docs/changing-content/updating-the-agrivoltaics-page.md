# Updating the agrivoltaics page

This guide will walk you through the process of updating the agrivoltaics page on the CERG website. Most of this is also a duplicate from updating the homepage.

You can edit the Agrivoltaics page through this link below. 

!!! info "Prerequisite"
    You must be signed into your SFU account and have access to AEM in order to make changes. If you do not have access, please [contact Andy](mailto:ahira@sfu.ca) to request access.

[Go to Agrivoltaics page on AEM :material-arrow-top-right-thick:](https://author.sfu.ca/cf#/content/sfu/politics/CERG/agrivoltaics.html){ .md-button .md-button--primary target="_blank"}



## Change the banner image
!!! info "Prerequisite"
    You have already uploaded the image to AEM that you want added to the banner. If you haven't done this yet, please follow the steps in [Uploading new photos and documents](../new-content/how-to-upload-new-photos-and-documents.md).

1. Double click on the banner image or right click and select `Edit`.
1. Select the `Image` tab.
1. Drag and drop a new image into the `Image` field from the sidebar. 
1. Press the `Crop` button to crop the image to a 3:1 (Banner) aspect ratio.
1. If you'd like to include a caption, select the `Advanced Image Properties` tab and enter your text in the Description text field.
1. Press the `OK` button and [Activate the page](../general/update-info-on-a-page.md#while-editing-inside-a-page) to save your changes.

<video controls width="100%">
  <source src="../video/changing a banner image (non-homepage).mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
/// caption
Changing the banner image on the Agrivoltaics page
///


## Update text content
1. Right click on the text you want to edit and select `Edit`.
1. Make your changes in the text editor that appears. 
1. Use the formatting buttons a the top of the editor to format your text, add links, or add images.
1. Press the `OK` button and [Activate the page](../general/update-info-on-a-page.md#while-editing-inside-a-page) to save your changes.

!!! warning "Text with `{{ }}`"
    Don't edit text inside `{{ }}` — it's a variable placeholder auto-filled by the site, and editing it breaks the component. 

    If that text needs to change (e.g., event, working paper, or news article info), update it via [the documentation for that content type](../new-content/adding-a-working-paper.md) instead; changes will automatically reflect on the Agrivoltaics page.

## Add a working paper
Please visit the page [Creating a new Working Paper](../new-content/adding-a-working-paper.md) to learn how to add a new working paper to the Agrivoltaics page.

Working papers tagged with the Agrivoltaics topic automatically appear on this page once published.


## Change photos in the photo gallery
Each photo gallery on our website is its own folder in AEM's DAM (Digital Asset Manager). To change the photos in the gallery, you will need to upload new photos to the folder and delete old ones.

[Go to the Agrivoltaics image gallery folder in DAM :material-arrow-top-right-thick:](https://author.sfu.ca/damadmin#/content/dam/sfu/politics/CERG/CERGImages/image-gallery/page-agrivoltaics){ .md-button .md-button--primary target="_blank"}

=== "Images already in DAM somewhere"

    1. Go into DAM and find the image(s) you want to add to the gallery. 
    2. Select the image(s), right click, and select the `Copy` button
    3. Navigate to the Agrivoltaics image gallery folder and select `Paste` to add the image(s) to the gallery.
    1. Reorder, delete, or edit the images in the gallery as needed. 
    1. Make sure you [activate the image(s)](../general/update-info-on-a-page.md#activate-an-image-or-document) to save your changes.

=== "Images not yet uploaded to DAM"

    1. Follow the instructions for [uploading new images to DAM first](../new-content/how-to-upload-new-photos-and-documents.md).
    2. Add a caption to the images if you want to (see instructions below).
    3. Copy the images to the Agrivoltaics image gallery folder using the [instructions in the first tab](#images-already-in-dam-somewhere).
    1. Make sure you [activate the image(s)](../general/update-info-on-a-page.md#activate-an-image-or-document) to save your changes.

### Adding captions
If you want to add captions to the images in the gallery, you can do so by editing the image properties in DAM.

1. Right click on the image and select `Open`.
1. Enter your text in the Description text field.

<video controls width="100%">
  <source src="../video/changing the photo gallery.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
/// caption
Changing the photo gallery's images on the Agrivoltaics page
///

## Update the video feed

Currently the Agrivoltaics page has a YouTube video feed that automatically pulls in videos from the Agrivoltaics playlist on CERG's YouTube channel. If you want to change the videos that appear on the feed, add new videos to that playlist.

[Agrivoltaics YouTube playlist :material-arrow-top-right-thick:](https://www.youtube.com/playlist?list=PLHSY2zpB60yE){ .md-button .md-button--primary target="_blank"}

Visit YouTube's documentation for more information on [how to add videos to a playlist :material-arrow-top-right:](https://support.google.com/youtube/answer/57792?hl=en){target="_blank"}.

!!! info "Playlist sorting"
    Currently, the videos in the playlist are sorted by "Date added (newest)". If you want to change the order of the videos, you can change the sorting method in the [playlist settings :material-arrow-top-right:](https://studio.youtube.com/playlist?list=PLHSY2zpB60yE/edit).

If you want to change this feed's behaviour (i.e. showing specific videos), follow [these instructions](yt-video-feeds.md).

## Add an event
Please visit the page [Creating an event](../new-content/how-to-add-an-event.md) to learn how to add a new event to the Agrivoltaics page.

Events tagged with the Agrivoltaics topic automatically appear on this page once published.

## Add a news article
Please visit the page [Creating a news item](../new-content/how-to-add-a-news-item.md) to learn how to add a new news item to the Agrivoltaics page.

News items tagged with the Agrivoltaics topic automatically appear on this page once published.


## Add a team member
!!! info "Prerequisite"
    You have already uploaded the image to DAM under the [CERG team folder :material-arrow-top-right:](https://author.sfu.ca/damadmin#/content/dam/sfu/politics/CERG/CERGImages/cerg-team){target="_blank"} and have created a team member page under [CERG Team :material-arrow-top-right:](https://author.sfu.ca/siteadmin#/content/sfu/politics/CERG/cerg-team){target="_blank"}.

If you want to add a new team member to the `Meet the team` section, you can copy and paste an existing member card and edit the information:

1. Right click on an existing team member card (i.e. Omri Haiven's) and select `Copy`.
1. Right click on the `Drag components and assets here` section that's below the existing cards and select `Paste`.
1. Change the information in the new card by right clicking on it and selecting `Edit`. Make sure to change the name, description, link text and URL, and image.
    1. Ensure the image is a square image (1:1 aspect ratio) and is cropped to the face of the team member.
1. Press the `OK` button and [Activate the page](../general/update-info-on-a-page.md#while-editing-inside-a-page) to save your changes.

<video controls width="100%">
  <source src="../video/adding a team member agrivoltaics.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
/// caption
Adding a team member preview card on the Agrivoltaics page
///

## Edit Current Partnerships section
As the current partnerships section is just a text block you can edit the text by right clicking on it and selecting `Edit`. More detailed instructions are [available here](#update-text-content).


## Add/remove a sponsor
!!! info "Prerequisite"
    In order to ensure proper sizing for all logos, please run your image through this [image resizer :material-arrow-top-right:](https://bulkresizephotos.com/en?preset=true&type=exact&width=1000&height=300&format=png){target="_blank"} before uploading it to DAM.

    Then you can proceed with uploading the logo to DAM under the [Logos folder :material-arrow-top-right:](https://author.sfu.ca/damadmin#/content/dam/sfu/politics/CERG/CERGImages/logos){target="_blank"}.


1. Ensure you have properly resized the logo and uploaded it to DAM under the Logos folder.
1. Duplicate an existing sponsor card by right clicking on it and selecting `Copy`.
1. Right click on the `Drag components and assets here` section that's below the existing cards and select `Paste`.
2. Edit the new card by right clicking on it and selecting `Edit`.
3. Change the image to the new sponsor's logo by dragging and dropping it from the sidebar.
4. Go to the `Advanced` tab and change the `Link to` field to the sponsor's website.
1. Press the `OK` button and [Activate the page](../general/update-info-on-a-page.md#while-editing-inside-a-page) to save your changes.

!!! warning "Place sponsor cards in the first two columns"
    Only place sponsor cards in the first two columns. The third column is reserved to preserve the mobile layout.

<video controls width="100%">
  <source src="../video/adding a new sponsor agrivoltaics.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
/// caption
Adding a new sponsor card on the Agrivoltaics page (does not show the resizing process)
///