## [WIP] Spotify Now-Playing Stream Overlay

#### What is this?

A small project that displays song currently playing

#### How to use?

1. Go to https://developer.spotify.com/dashboard and create your application.
   ![Step 1](assets/1.1.png)
   Your app details should be something like that. Click 'Save'.
   ![Step 1](assets/1.2.png)
2. Click on 'Settings'.
   ![Step 2](assets/2.1.png)
   You will be brought to this page.
   ![Step 2](assets/2.2.png)
   Click on 'View client secret'.
   ![Step 2](assets/2.3.png)
   Copy both the Client ID and Client secret values (censored on the screenshot).
3. Click on 'Code' and download the zip file (of course unzip it).
   You could also use git, run `git clone "https://github.com/caffeinated01/Now-Playing-Overlay"`.
   ![Step 3](assets/3.png)
4. Right click on the folder, then press 'Open in Terminal' then run `pip install -r requirements.txt` also, rename the template file to '.env' and replace the ID and secret values from earlier.
   ![Step 4](assets/4.png)
5. Run the code - in the terminal, run `python app.py` then CTRL+CLICK on the link (http://127.0.0.1:5000 in the case of the screenshot).
   ![Step 5](assets/5.png)
6. Add a 'Browser Source'
   Click 'Add a new source instead', and 'Add Source'. Under URL, enter the link from the previous step. Under 'Width' and 'Height' enter 800 and 150 respectively.
   ![Step 6](assets/6.png)

7. All set! When you want to stop the program, go back to terminal and press CTRL+C. Note that the overlay only works when you are running it in the terminal.

#### How to configure?

Coming soon...

#### TODO

- [] Customisability for how overlay looks
- [] Customisability for backend
