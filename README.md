# Obsidian Blogging Template

## The Minimal Definition of Documentation

### Setup

> **This Only Applies for OSX/Macs/Apple**

1. Install Obsidian on devices:
    - https://obsidian.md
2. Create a vault.
3. Right click and make sure the vault folder has keep downloaded checked.
    - make sure you do this on iOS too.
4. Make a folder called blog or whatever you want.
5. Enable Community Plugins.
6. Install obsidian-git.
    - Also potentially called git.
7. Make a GitHub repo from this template.
8. Create a personal access token.
8. When prompted for repo in obsidian-git use:
    - https://<PAT_TOKEN>@my_ssh_repo_url
9. The folder should be the one created in step 3.
10. Once repo has been cloned. Find iCloud folder called blog or whatever and open terminal at location.
11. Run:
```
git checkout obsidian
```
12. Double check this! You want to make sure you are sending posts to the Obsidian branch.
    - If you don't everything you say and do will be public near instantaneously.
13. Configure and enable Unique Note Creator.
    - file location can point to _drafts or another staging folder.
    - create a folder called templates or something.
        - make a template with the following yaml:
        ```
        ---
        title:
        description:
        layout: posts
        ---
        ```
        - set prefix format to: YYYY-MM-DD
14. Create a Fly.io account.
15. Create a Fly.io deploy token.
16. Add token to Settings > Secrets > Actions > FLY_API_TOKEN.
17. Add css. Make it yours and pretty!
    - There's also a few templates that should work with this:
        - https://github.com/maximevaillancourt/digital-garden-jekyll-template
        - https://github.com/oleeskild/digitalgarden
18. Edit the following:
    - ```_config > url: "URL YOU HOST AT"```
    - ```ngnix.conf > server_name <FILL THIS IN>;```
        - This should be your domain name.
    - ```_layouts/default.html > <!-- <link rel="icon" type="image/png" href=""/> -->```
        - Everyone needs a favicon
19. Follow directions starting from here for initial deployment.
    - https://fly.io/docs/languages-and-frameworks/static/#configuring-the-app-for-fly-io

### Usage
#### Obsidian
1. cmd + p > create new unique note
    - Editing the header will change the file name.
    - The file name will create the date and url of the post.
2. Write things.
3. Right click and stage changes.
4. Open right side menu and commit changes.

#### IDE
5. Go to IDE of choice.
6. Change to obsidian branch.
7. Run:
```
bundle exec jekyll s
```
8. Review and make changes in either Obsidian or IDE.
    - Optional for images: 
        - Create python venv and install requirements.
            - ```source venv/bin/activate```
        - Put images in ```raw_images```.
        - Run:
            ```
            python image-conversion.py
            ```
        - Delete images if you want.
        - Alternative is to keep images in ```raw_images``` and let the GitHub Action do the same.
            - Only downside is your repo will fill up with large images.
9. If all looks good. Commit any last changes and create a PR comparing obsidian to main.
10. Merge your obsidian branch.
    - Do not delete!
11. Watch your site update.
