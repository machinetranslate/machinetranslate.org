*This README is for adding events to machinetranslate.org.*

## JSON files

There are three types of JSON files used for adding events:

- events.json: This file is used for adding all events except for WMT events.
- wmt_events.json: Specifically for adding WMT (Workshop on Machine Translation) events.
- calls_for_papers.json: For adding external events that have calls for papers and don't have an entry in events.json or wmt_events.json.


## How to add events

To add an event, follow these steps:

> 1. Navigate to the [Event Form](https://machinetranslate.github.io/add-data/)
> 2. Select the type of event you want to add (i.e., Events, WMT events, or Calls For Papers).
> 3. Fill in the fields with event details.
> 4. Click on the "Submit" button.
> 5. The tool will generate a JSON representation of your event.
> 6. Copy the generated JSON.
> 7. Paste the JSON into the corresponding `.json` file based on the type of event:
    - For regular events, paste it into `events.json.`
    - For WMT events, paste it into `wmt_events.json.`
    - For calls for papers, paste it into `calls_for_papers.json.`
> 8. Run ```Python generate.py``` to genarate the event. 

That's it! Your event has been added.


## Additional tips on adding events

Sometimes, there might be additional details or information related to an event that aren't covered by the standard fields in the form, you can manually add it inside the `.md` file that gets created after following the steps mentioned above. Simply open the generated `.md` file and add the extra details as you would inside a standard Markdown file.