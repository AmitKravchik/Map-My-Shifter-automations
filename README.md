# Map-My-Shifter-automations
Selenium automations on IBM's Map My Shifter website: https://ibm.github.io/map-my-shifter/#/

# AutomationFromStixReport:
1. Running on this webpage: https://ibm.github.io/map-my-shifter/#/from_stix 
2. Uploading any from_stix_map json file from each module of STIX shifter.
3. For each module and file, Outputting which STIX object's feilds has a mapping, and which doesn't, based on the HTML class attribute extension.
4. The output is a json in the following scheme: Module -> from-stix-map file name -> STIX object -> fields.

# How to use:
1. Change DRIVER_PATH to your local chrome driver path.
2. Change BASE_PATH to your local stix-shifter_modules directory.
3. Change OUTPUT_FILE_PATH to the path you want to output the results.

# An example of the output:

"aws_athena": {
        "guardduty_from_stix_map.json": {
            "Artifact": {
                "existingFields": [
                    "payload_bin"
                ],
                "notExistingFields": [
                    "mime_type",
                    "url",
                    "hashes.SHA-256",
                    "hashes.MD5",
                    "hashes.SHA-1"
                ]
            },
            "AS": {
                "existingFields": [],
                "notExistingFields": [
                    "number (*)",
                    "name",
                    "rir"
                ]
            },
            "Directory": {
                "existingFields": [],
                "notExistingFields": [
                    "path (*)",
                    "path_enc",
                    "created",
                    "modified",
                    "accessed"
                ]
  }
