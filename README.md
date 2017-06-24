# piband
This is the website for the Piband, a wearable DIY necklace made with a Raspberry Pi that can answer questions, tell you the news, etc. This is a list of the stuff you can do with it:

-Timers/alarms/time/date

-Dictionary/thesaurus

-XKCD transcripts

-Music

-Summoning Cthulu (reads the call of Cthulu in a loud scary voice)

-News

-Translate

-General Knowledge questions (e.g. "what's the capital of Australia", "how many ounces in a cup")

And much, much more coming soon!

And this is a list of all the API's I use:

-[Yandex Translate](http://translate.yandex.com)

-[Big huge Thesaurus](https://words.bighugelabs.com/api.php)

-[Dictionary.reference.com](https://dictionary.reference.com)

-[Wolfram Alpha](https://www.wolframalpha.com/)

-[Xkcd API](https://xkcd.com)

-[Newsapi.org](https://newsapi.org)

The Piband is open source and fully customizable and additional scripts can be made by either editing the source code locally or creating python scripts, for example the [news script](https://github.com/bobmonkeywarts/piband/blob/master/src/news.py). This script is in a seperate file and can be started by the main script, piband.py. Then, when the user says "script news", it runs your custom script, making it an ideal platform for makers who want to add on to their virtual assistants.


Video at https://tinyurl.com/the-piband! Github repository at https://github.com/bobmonkeywarts/piband.
