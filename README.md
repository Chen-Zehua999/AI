# Word to Markdown Converter with Text-Image Tables

This Python script converts Word documents (.docx) to Markdown format, specifically creating 1x2 tables where:
- First row contains text content
- Second row contains the image that appears below that text

## Features

- ✅ Converts .docx files to Markdown
- ✅ Extracts text and images from Word documents
- ✅ Creates 1x2 tables with text-image pairs
- ✅ Saves images as separate files with proper linking
- ✅ Maintains document structure while reformatting content
- ✅ Optional conversion back to Word format
- ✅ Automatic dependency installation

## Requirements

The script automatically installs the following Python packages:
- `python-docx` - For reading Word documents
- `mammoth` - For better Word document conversion with image support
- `markdown` - For Markdown processing
- `docx2txt` - For text extraction fallback

## Usage

### Basic Usage
```bash
python3 docx_to_markdown_converter.py
```
This will convert the default file `Linux/0. Set up of LAN Segments.docx` to Markdown format.

### Specify Input File
```bash
python3 docx_to_markdown_converter.py "path/to/your/document.docx"
```

### Specify Output File
```bash
python3 docx_to_markdown_converter.py "input.docx" --output "output.md"
```

### Convert Back to Word
```bash
python3 docx_to_markdown_converter.py "input.docx" --to-word
```

### Install Dependencies Only
```bash
python3 docx_to_markdown_converter.py --install-deps
```

### View Help
```bash
python3 docx_to_markdown_converter.py --help
```

## Output

The script generates:
1. **Markdown file** (.md) - Contains the converted content with text-image tables
2. **Images directory** (_images) - Contains extracted images as separate PNG files
3. **Word file** (.docx) - Optional reconverted Word document

## Example Output

The script creates tables like this:

```markdown
| Content |
|---------|
| This will be the network topology that will be referenced for setting up the infrastructure. |
| ![Image 1](0. Set up of LAN Segments_images/0. Set up of LAN Segments_image_01.png) |
```

## Example Run

```bash
$ python3 docx_to_markdown_converter.py
Converting 'Linux/0. Set up of LAN Segments.docx' to 'Linux/0. Set up of LAN Segments.md'...
Installing required dependencies...
✓ python-docx already installed
✓ mammoth already installed
✓ markdown already installed
✓ docx2txt already installed
Reading Word document...
✓ Conversion completed successfully!
Output saved to: Linux/0. Set up of LAN Segments.md
Images saved to: Linux/0. Set up of LAN Segments_images
```

## File Structure

After running the script, you'll have:
```
Linux/
├── 0. Set up of LAN Segments.docx (original)
├── 0. Set up of LAN Segments.md (converted)
└── 0. Set up of LAN Segments_images/
    ├── 0. Set up of LAN Segments_image_01.png
    ├── 0. Set up of LAN Segments_image_02.png
    └── ... (additional images)
```