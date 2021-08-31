# what3words-addresses-within-a-specific-area

According to [this faq](https://support.what3words.com/en/articles/4170913-can-i-download-a-list-of-words-or-what3words-addresses-that-meet-certain-conditions) it is not possible to download what3words addresses within a specific area. Well now it is.

## Warning

This uses the API that the w3w website uses, not the API that 3rd party devs are supposed to use. That probably means that use of this tool is agains w3w's terms of service.

## Another Warning

This may or may not work for locations in the southern hemisphere or to the east of the prime meridian. I just haven't tested it.

## Usage

`./w3w-area.py <LATITUDE>,<LONGITUDE> <AREA-SIZE>`

### Example usage:

```
$ ./w3w-area.py 51.520847,-0.195521 3
///filled.count.soap
///mount.newly.that
///atom.token.lame
///poppy.hooks.shower
///sleep.bend.incomes
///news.engine.hunter
///gets.herb.phones
///deed.tulip.judge
///broker.manual.hungry
```
