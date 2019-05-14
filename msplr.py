# pylint: disable=C0301
# pylint: disable=C0111
import subprocess  # Used to get the artist playing and the title of the song playing.

def main():

    """
    Main function to do everything that is needed.
    First, it gets the status of the player.
    If something is playing, it prints the artist and title of the currently playing track.
    If that is an advertisement, it does some special magic tricks to get rid of the brainwashing.
    If something is NOT playing, it requires music.
    """
    proc = subprocess.run(['playerctl', 'status'], encoding='utf-8', stdout=subprocess.PIPE, stderr=subprocess.STDOUT)  # Gets the current status of the player, and outputs it to proc.stdout.
    proc = proc.stdout.replace("\n", "")  # Sets the variable proc to be the output of the above, removing useless data.

    if proc == "No players found":  # If there is no player found:
        print("Wanted: Music Player")  # Prints random message asking for a player

    else:  # If a player *is* found
        if proc == "Playing":  # If a music player is playing:
            artist = subprocess.run(['playerctl', 'metadata', 'artist'], encoding='utf-8', stdout=subprocess.PIPE)  # Gets the current name of the artist playing, and outputs it to artist.stdout.
            artist = artist.stdout.replace("\n", "")  # Sets the variable artist to be the output of the above, removing useless data.

            title = subprocess.run(['playerctl', 'metadata', 'title'], encoding='utf-8', stdout=subprocess.PIPE)  # Gets the title of the track playing, and outputs it to title.stdout.
            title = title.stdout.replace("\n", "")  # Sets the variable title to be the output of the above, removing useless data.

            if title in ('Advertisement', 'Spotify'):  # If an advertisement is currently playing:
                print("Brainwashing in Process.")  # Prints the truth of spotify's plans.
                subprocess.run(['amixer', '-q', 'set', 'Master', 'mute'], encoding='utf-8')  # Mutes the master audio until brainwashing is over.
            else:  # If the currently playing track is NOT an advertisement:
                print("{} - {}".format(title, artist))  # Prints the title and artist.
                subprocess.run(['amixer', '-q', 'set', 'Master', 'unmute'], encoding='utf-8')  # Unmutes the master audio if it was auto-muted by the anti-brainwashing process.

        else:  # If music is NOT playing:
            print("Error: Music Needed")  # Require that music be played.


main()  # Calls the main function
