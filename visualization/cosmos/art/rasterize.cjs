// Usage: node visualization/cosmos/art/rasterize.cjs input.svg output.png
// Uses the installed Codex primary runtime; no Inkscape/rsvg delegate required.
const sharp=require(process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES+'/sharp');
sharp(process.argv[2]||__dirname+'/contact-sheet.svg').png().toFile(process.argv[3]||__dirname+'/contact-sheet.png').catch(e=>{console.error(e);process.exitCode=1;});
