# BST236 Assignment - Copilot Instructions

## Project Overview

This is a personal portfolio website (BST236 course assignment) showcasing web development projects. The site features a cyberpunk/neon aesthetic with dark backgrounds, pink/cyan accents, and custom cursors.

**Current structure:**
- `index.html` - Main portfolio homepage with project cards
- `pacman/index.html` - Standalone Valentine's Day themed Pac-Man game
- Future: `arxiv/` directory (planned arXiv paper feed project)

## Architecture

### Single-File Applications
Each project is a **self-contained single HTML file** with embedded CSS and JavaScript. No build process, no external dependencies, no frameworks - just vanilla HTML5/CSS3/JavaScript.

**Why this approach:**
- Projects are assignments meant to be standalone and portable
- Each project lives in its own directory with one `index.html` file
- All styles go in `<style>` tags, all scripts in `<script>` tags
- Navigation between projects uses relative paths (`../`, `./pacman/index.html`)

### Pac-Man Game (`pacman/index.html`)
- **Grid-based movement system**: 28×31 tile maze with pixel interpolation for smooth animation
- **Game loop**: `requestAnimationFrame` with delta-time for consistent speed
- **Collision detection**: Tile-based using 2D array (`maze[y][x]`)
- **Entity structure**: JavaScript objects with `gridX/gridY` (tile position) and `pixelX/pixelY` (rendered position)
- **State machine**: `gameState.screen` cycles through: `'start'` → `'playing'` → `'gameover'/'win'`
- **Rose power-up system**: Spawns every 15-20s, enables 8s powered state with auto-firing heart projectiles
- **Ghost AI types**: Red (chase), Cyan (ambush), Orange (random) - all grid-based pathfinding

## Key Conventions

### Visual Theme Consistency
- **Background color**: `#0a0a12` (dark cyberpunk black) used across all pages
- **Neon accents**: Cyan (`#00f0ff`), Magenta/Pink (`#ff69b4`), Purple (`#b000ff`)
- **Typography**: 
  - Headings: `'Orbitron'` (techy/futuristic)
  - Body: `'Rajdhani'` (clean sans-serif)
  - Code/mono: `'Fira Code'`
- **Interactive elements**: Hover effects with neon glow using `box-shadow` and color transitions

### Code Style (JavaScript)
- Use `const` for constants and immutable references, `let` for variables
- Functions are declared with `function` keyword (not arrow functions for top-level game functions)
- Canvas operations: Store 2D context as `ctx`, always clear with `ctx.clearRect()` before drawing
- Game entities: Objects with properties like `gridX`, `gridY`, `pixelX`, `pixelY`, `direction`, `speed`
- Direction handling: String-based (`'up'`, `'down'`, `'left'`, `'right'`), mapped to vectors in `DIRECTIONS` object

### Canvas Rendering Patterns
```javascript
// Standard entity draw pattern
ctx.save();
ctx.translate(entity.pixelX, entity.pixelY);
// ... draw shape ...
ctx.restore();
```

### Maze Data Structure
```javascript
// 0 = wall, 1 = pellet, 2 = empty path, 3 = ghost house
const ORIGINAL_MAZE = [
    [0, 0, 0, ...],
    [0, 1, 1, ...],
    // 28 tiles wide × 31 tiles tall
];
```

### File Paths & Navigation
- Homepage links to projects: `./pacman/index.html`
- Projects link back: `<a href="../">← Back to Home</a>`
- Future projects follow same pattern: `./project-name/index.html`

## Development Workflow

**No build tools required** - just open `index.html` in a browser.

For testing Pac-Man game changes:
1. Edit `pacman/index.html` 
2. Refresh browser (Cmd+R / Ctrl+R)
3. Use browser DevTools console for debugging game state

**Testing game state:**
```javascript
// In browser console while game is running:
console.log(pacman);      // Check Pac-Man position/state
console.log(ghosts);      // Check ghost states
console.log(gameState);   // Check score/lives/screen
console.log(hearts);      // Check active projectiles
```

## Common Patterns

### Adding New Project Cards (Homepage)
```html
<a href="./new-project/" class="card reveal">
    <span class="card-icon">🎮</span>
    <div class="card-tag">Category</div>
    <h3>Project Name</h3>
    <p>Description...</p>
    <span class="card-arrow">↗</span>
</a>
```

### Game Entity Movement (Pac-Man style)
1. Store target tile in `gridX`/`gridY`
2. Interpolate `pixelX`/`pixelY` toward `gridX * TILE_SIZE`
3. When close enough (`< tolerance`), snap to grid and check next direction
4. Check `canMove(newGridX, newGridY)` before committing to new tile

### Collision Detection
- **Tile-based**: `maze[entity.gridY][entity.gridX]` 
- **Entity vs Entity**: Check if `gridX`/`gridY` match or `distance < threshold`
- **Projectile vs Wall**: Check tile at `heart.pixelX / TILE_SIZE`, `heart.pixelY / TILE_SIZE`

## Assignment Context

This is homework for **BST236** (likely a web development/programming course). Each project is a separate assignment meant to demonstrate different skills:
- **Pac-Man**: Game dev, Canvas API, event handling, game loops, collision detection
- **arXiv Feed** (planned): Data fetching, API integration, automation

When adding new projects, follow the single-file pattern and maintain the cyberpunk aesthetic.
