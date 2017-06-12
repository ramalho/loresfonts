# low-res-fonts
Low resolution bitmapped fonts in LRF format

## About LRF

LRF (Low Resolution Font) is a simple bitmapped font format designed to make it easy to display on scrolling LED-matrix displays, because the pixels for each glyph are organized by column. For example, in a 7x8 font like that of the Apple ][, the glyph for the capital F is stored like this:

```
00000000
01111111
00001001
00001001
00001001
00000001
00000000
```

### LRF headers

LRF is a binary format. An LRF version 1 file has a header, followed by glyph records with the bitmap for each character shape.

The header contains:

- MAGIC: the ASCII letters "LRF1" (four bytes);
- CW: One unsigned byte with the character code width, ex. 2 if the character code in each glyph record is a 2-byte unsigned integer;
- GW: One unsigned byte with the glyph width, ex. 7 for a 7x8 font;
- GH: One unsigned byte with the glyph height, ex. 8 for a 7x8 font (see note below);
- NG: One unsigned short integer (2 bytes, big-endian) with the number of glyphs in the font.

> **NOTE:** LRF version 1 supports a maximum glyph height of 8;
> therefore the value of GH is always <= 8.

### LRF glyph records

Each glyph record contains:

- CW bytes with the Unicode character code for the glyph in big-endian order, ex. 0x0041 for "A", Unicode U+0041;
- GW bytes, each holding the bitmap for one pixel column.

#### Examples

Given a LRF1 file with a 7x8 font where each character code is one byte, each glyph record has 8 bytes: 1 byte for the character code and 7 bytes for the 7 pixel columns that make up the glyph. In such a file:

- The glyph record for the "|" (pipe or vertical bar) character is `7C 00 00 00 FF 00 00 00`, where 0x7f represents the Unicode character code for _VERTICAL LINE_ (U+007F), 0x00 are blank columns and 0xFF are the 8 pixels of a full-height vertical line (11111111).

- The glyph record for the "\_" (underscore or low line) character is `5F` followed by `80` repeated 7 times, where 0x5F stands for U+005F (Unicode character named _LOW LINE_) and each 0x80 represents a single pixel set at the bottom of a column with the remaining pixels unset (10000000).
