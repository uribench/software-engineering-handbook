# Illustration: It's payback time
Often, development is tight (when is it not!). Corners are cut to deliver software 'on time'. 
Sometimes this works, we re-pay the cut-corners and the software remains maintainable. 
Sometimes, quality issues and other factors cause delay. It takes more time to reach production due to compromised quality. These quality issues are remembered long after delays are forgotten.

## What takes away effort from innovation?
When small changes require complex analysis and elaborate test-cycles, you know some debt has accumulated. Was it because of pressure? An illusion of pressure? Developer didn't know his job? *Does it really matter?* Any debt or asset has a limiting effect. Buying a car takes longer if the one in the garage needs to be sold.
Similarly, writing code takes longer if there's some existing code. Or is that true?

## Let's explore with a small illustration
Think of a feature that requires multiple parts of the system. When one of those parts isn't available, the feature isn't available. However, the UI-widget that gives access to the feature remains enabled, even when the feature isn't available. So there's a request now to disable the button when the feature isn't available. 
The logic we want to write may look like:
```
parts_state = fetch_parts_availability()
button_state = function_is_relevant(parts_state)
button.set_state(button_state)
```
My work is the piece called `function_is_relevant`. It would be small and should take a few minutes to write.

However, in any production code, there are some 'extras' to be done. These are **elements of design**, particular to this piece of work:
* What's the request? Have I understood correctly?
* How do I get the data? Can I make a blocking call there?
* What if there's an error?
* When do I enable it again?

There's another family of 'extras'. Mostly repetitive **waste** that can be taken out:
* How do I configure the `fetch_parts_availability` function to work? 
* Does that function really do what I think it does?
* How should I setup the build environment?
* How do I test? What should I test? Maybe I need to wait for a fully installed test system, because I cannot see the UI on a developer system.

### Here's a possible sequence of development:

|Day 1|Day 2|Day 3|Day 4|Day 5|
| --- | --- | --- | --- | --- |
|Try to read old code, ask around, change & build|Find test system and install new build|Notice failures. Figure out if they 'already existed'|Fix issues that are fixable|Find and setup test system again...|

(and we're still unsure if we understood everything...)

### Is there a better way?
How about using the **elements of design** to get rid of some waste?

|Day 1|Day 2|Day 3|Day 4|Day 5|
| --- | --- | --- | --- | --- |
|Clarify intended behavior, use a system and iterate a few quick trials|Mock `fetch_parts_availability`, write a small driver|Code, test and fix at your desk, several times a day is required|Find and setup test system|Fix integration issues, strengthen the test driver|

While the second method takes the same time, we now have better understanding. What's more, we've coded our understanding in a test. If you have friends in the CI/CD team, they would make the test run on every build. You have started an approach that will help maintenance efforts in years to come!

In future, whenever things related to part-availability change, developers can iterate freely and be confident that the code delivered will work at the end of their day.

## What just happened?
Congratulations, you have paid back some debt! And you didn't need another loan to do that. Was it your debt to pay? Was the 'second approach' your responsibility anyway? **It doesn't really matter**. Try it and see :)
