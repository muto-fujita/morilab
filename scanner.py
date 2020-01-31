import subprocess
import sys
import time

"scanimage -L" #show available scaner

'''
All options specific to device `epson2:libusb:001:003':
  Scan Mode:
    --mode Lineart|Gray|Color [Lineart]
        Selects the scan mode (e.g., lineart, monochrome, or color).
    --depth 8|12|14|16bit [inactive]
        Number of bits per sample, typical values are 1 for "line-art" and 8
        for multibit scans.
    --halftoning None|Halftone A (Hard Tone)|Halftone B (Soft Tone)|Halftone C (Net Screen)|Dither A (4x4 Bayer)|Dither B (4x4 Spiral)|Dither C (4x4 Net Screen)|Dither D (8x4 Net Screen)|Text Enhanced Technology|Download pattern A|Download pattern B [Halftone A (Hard Tone)]
        Selects the halftone.
    --dropout None|Red|Green|Blue [None]
        Selects the dropout.
    --brightness -4..3 [0]
        Selects the brightness.
    --sharpness -2..2 [0]
    --gamma-correction Default|User defined|High density printing|Low density printing|High contrast printing [Default]
        Selects the gamma correction value from a list of pre-defined devices
        or the user defined table, which can be downloaded to the scanner
    --color-correction None|Built in CCT profile|User defined CCT profile [Built in CCT profile]
        Sets the color correction table for the selected output device.
    --resolution 50|60|72|75|80|90|100|120|133|144|150|160|175|180|200|216|240|266|300|320|350|360|400|480|600|720|800|900|1200|1600|1800|2400|3200|4800|6400|9600|12800dpi [25]
        Sets the resolution of the scanned image.
    --threshold 0..255 [128]
        Select minimum-brightness to get a white point
  Advanced:
    --mirror[=(yes|no)] [no]
        Mirror the image.
    --auto-area-segmentation[=(yes|no)] [yes]
        Enables different dithering modes in image and text areas
    --red-gamma-table 0..255,... [inactive]
        Gamma-correction table for the red band.
    --green-gamma-table 0..255,... [inactive]
        Gamma-correction table for the green band.
    --blue-gamma-table 0..255,... [inactive]
        Gamma-correction table for the blue band.
    --wait-for-button[=(yes|no)] [no]
        After sending the scan command, wait until the button on the scanner
        is pressed to actually start the scan process.
  Color correction:
    --cct-type Automatic|Reflective|Colour negatives|Monochrome negatives|Colour positives [inactive]
        Color correction profile type
    --cct-profile -2..2,...
        Color correction profile data
  Preview:
    --preview[=(yes|no)] [no]
        Request a preview-quality scan.
  Geometry:
    -l 0..215.9mm [0]
        Top-left x position of scan area.
    -t 0..297.18mm [0]
        Top-left y position of scan area.
    -x 0..215.9mm [215.9]
        Width of scan-area.
    -y 0..297.18mm [297.18]
        Height of scan-area.
  Optional equipment:
    --source Flatbed|Transparency Unit|TPU8x10 [Flatbed]
        Selects the scan source (such as a document-feeder).
    --auto-eject[=(yes|no)] [inactive]
        Eject document after scanning
    --film-type Positive Film|Negative Film|Positive Slide|Negative Slide [inactive]
    --focus-position Focus on glass|Focus 2.5mm above glass [Focus on glass]
        Sets the focus position to either the glass or 2.5mm above the glass
    --bay 1|2|3|4|5|6 [inactive]
        Select bay to scan
    --eject [inactive]
        Eject the sheet in the ADF
    --adf-mode Simplex|Duplex [inactive]
        Selects the ADF mode (simplex/duplex)
'''

def scan(option, save_as):
    """
    スキャン画像から4つのプレートを切り出す
    img = img[y:y+height,x:x+width]

    Parameters
    ----------
    option : chair[]
        ['--resolution', '360', '--mode', 'Color']
        ↑みたいな配列
    save_as : chair
        保存名
    """
    cmd = ["scanimage"]
    cmd.extend(option)

    with open(save_as, "w") as f:
        subprocess.check_call(cmd, stdout=f)


if __name__ == '__main__':
    option = "--resolution 360\
    --mode Color\
    --source TPU8x10\
    --format=tiff".split()
    save_as = "a.tiff"
    scan(option, save_as)