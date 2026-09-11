# Updating the homepage
[Go to homepage in AEM :material-arrow-top-right-thick:](https://author.sfu.ca/cf#/content/sfu/politics/CERG.html){ .md-button .md-button--primary target="_blank"}


## Change the banner images
!!! info "Prerequisite"
    Ensure the image(s) you want added to the banner have already been uploaded to AEM. If not, follow the steps in [Uploading new photos and documents](../new-content/how-to-upload-new-photos-and-documents.md).

Due to AEM's limitations, the banner is a carousel of images on desktop, and one static image on mobile. Each has its own way of changing the images.

### Change the desktop carousel images
Each banner image on the website is its own unlisted page on the site. To change an image, you will need to edit the image property of the page.

[Go to homepage carousel folder in AEM :material-arrow-top-right-thick:](https://author.sfu.ca/siteadmin#/content/sfu/politics/CERG/homepage-banner-test){ .md-button .md-button--primary target="_blank"}

!!! tip "Tip: Image order in the carousel matches the page order in AEM"

#### Changing the image
1. In the Homepage Banner folder, select the page for the carousel image you want to change.
1. Right click on the page and select `Page Properties`.
1. Select the `Image` tab.
1. Drag and drop a new image into the `Image` field from the sidebar.
1. Press the `Crop` button to crop the image to a **3:1 (Banner)** aspect ratio.

#### Adding a caption
1. Still in `Page Properties`, select the `Basic` tab.
1. Expand the `More Titles and Descriptions` section.
1. Enter your caption in the `Description` field with a prefix of `Image:`. 
1. Press the `OK` button and [Activate the page](../general/update-info-on-a-page.md#while-in-wcm) to save your changes.

<video controls width="100%">
  <source src="../video/changing a carousel image (homepage).mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
/// caption
Changing an image on the homepage carousel
///

### Add new images to the desktop carousel
To add more images to the carousel, simply duplicate one of the existing pages in the Homepage Banner folder, then change the image and caption as described above. The new page will automatically appear in the carousel.


### Change the mobile banner image
To change the mobile banner image, you will need to edit the image directly [on the homepage :material-arrow-top-right:](https://author.sfu.ca/cf#/content/sfu/politics/CERG.html){target="_blank"}.



#### Changing the image
1. Narrow your browser window to a mobile size until you can see the mobile banner image.
1. Right click on the banner and select `Edit`.
1. Expand your browser window back to full size. The mobile banner image will still be selected.
1. Select the `Image` tab.
1. Drag and drop a new image into the `Image` field from the sidebar.
1. Press the `Crop` button to crop the image to a **3:2 (Carousel)** aspect ratio.

#### Adding a caption to the image
1. Select the `Advanced Image Properties` tab.
1. Enter your caption in the `Description` field with a prefix of `Image:`. 
1. Press the `OK` button and [Activate the page](../general/update-info-on-a-page.md#while-editing-inside-a-page) to save your changes.

<video controls width="100%">
  <source src="../video/changing mobile banner image (homepage).mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
/// caption
Changing the homepage banner's mobile image
///

## Change events on the homepage
!!! info "Prerequisite"
    Ensure the events you want added to the homepage have already been created in AEM. If not, follow the steps in [Creating an event](../new-content/how-to-add-an-event.md).

Currently due to AEM's limitations, the events section on the homepage must be manually updated.

### Change which events are shown
1. Right click on the events cards component and select `Edit`.
1. Go to the `Fixed list` tab.
1. Click the search icon to find the event you want to replace existing events on the homepage.
1. Click the `Add Item` button to add to the list on the homepage.
1. Ensure events are ordered by their dates. Use the green up and down arrows to reorder them if necessary.
1. Press the `OK` button and [Activate the page](../general/update-info-on-a-page.md#while-editing-inside-a-page) to save your changes.

### Change how many events are shown
As of writing, the homepage has been set to show four events in view. Any extra events will be paginated :material-information-outline:{ title="Pagination Definition: Help users navigate forwards and backwards through a series of content. For example, search results or a list of products."}. The user clicks the next button to view the next four events.

=== "To paginate after 2 events"

    1. While editing the events cards component, select the `List` tab.
    1. Change the `Pagnate after` field to `2`.
    1. Change the `CSS Class` field to `col-2 mds-stack outline`.

=== "To paginate after 3 events"

    1. While editing the events cards component, select the `List` tab.
    1. Change the `Pagnate after` field to `3`.
    1. Change the `CSS Class` field to `col-3 md-stack outline`.

=== "To paginate after 4 events"

    1. While editing the events cards component, select the `List` tab.
    1. Change the `Pagnate after` field to `4`.
    1. Change the `CSS Class` field to `col-2 mds-stack outline`.

<video controls width="100%">
  <source src="../video/changing events on homepage.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
/// caption
Changing which events are shown on the homepage and how many events are shown before pagination
///

## Add/change the team member cards in "Meet the Team"
Follow the instructions under [Updating the Agrivoltaics page](updating-the-agrivoltaics-page.md#add-a-team-member). It is the same process for changing the team member cards on the homepage.

## Updating the "Our Latest Work" section
This section has been set to automatically show the latest **modified** publication. Once you [create a new Working Paper](../new-content/adding-a-working-paper.md) or [op-ed](../new-content/how-to-add-a-new-op-ed.md), it should automatically appear in this section.

!!! warning "Ensuring the latest working paper appears in this section"
    If you change any past working paper and activate it, it will overwrite the latest published working paper. 

    You will need to go back and re-activate the latest working paper to ensure it appears in this section.


## Updating the "Our Latest Videos" section
Currently the homepage automatically displays the latest videos uploaded to the CERG's YouTube channel. Simply upload videos to the CERG YouTube channel and they will automatically appear in this section.

If you want to change this behaviour, follow [these instructions](yt-video-feeds.md).

## Updating the "Ways to connect" section
This section displays links to our social media profiles and contact us page. To add or change links, simply edit the text box and add a new link on a new line.