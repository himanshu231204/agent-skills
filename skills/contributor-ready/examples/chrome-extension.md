# Chrome Extension Project Example

This example demonstrates how to use contributor-ready with a Chrome extension project.

## Project Structure

```
my-chrome-extension/
├── src/
│   ├── background/
│   │   └── index.ts
│   ├── content/
│   │   └── index.ts
│   ├── popup/
│   │   ├── popup.html
│   │   ├── popup.ts
│   │   └── popup.css
│   ├── options/
│   │   ├── options.html
│   │   ├── options.ts
│   │   └── options.css
│   ├── components/
│   │   ├── Button.ts
│   │   └── Modal.ts
│   ├── utils/
│   │   ├── storage.ts
│   │   └── api.ts
│   └── types/
│       └── index.ts
├── public/
│   ├── icons/
│   │   ├── icon16.png
│   │   ├── icon48.png
│   │   └── icon128.png
│   └── manifest.json
├── tests/
│   ├── background.test.ts
│   ├── content.test.ts
│   └── popup.test.ts
├── docs/
│   └── development.md
├── package.json
├── tsconfig.json
├── webpack.config.js
├── README.md
├── LICENSE
└── .github/
    └── workflows/
        └── ci.yml
```

## Detection

When analyzing a Chrome extension project, contributor-ready detects:

- **Type**: Chrome extension (by manifest.json)
- **Language**: TypeScript or JavaScript (by file extensions)
- **Package Manager**: npm, yarn, or pnpm (by lock files)
- **Build System**: Webpack or Vite
- **Testing**: Jest or Vitest

## Generated Files

### README.md

```markdown
# my-chrome-extension

A Chrome extension for {description}.

## Features

- **Feature 1** — {description}
- **Feature 2** — {description}
- **Feature 3** — {description}

## Installation

### From Chrome Web Store

1. Visit the [Chrome Web Store](https://chromewebstore.google.com/detail/my-extension/{extension-id})
2. Click "Add to Chrome"
3. Confirm the installation

### From Source (Developer Mode)

1. Download or clone this repository
2. Open Chrome and go to `chrome://extensions/`
3. Enable "Developer mode" (toggle in top right)
4. Click "Load unpacked"
5. Select the `dist` folder from this repository

## Usage

### Basic Usage

1. Click the extension icon in the toolbar
2. Use the popup to interact with the extension
3. Configure settings in the options page

### Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+Shift+X` | Open popup |
| `Ctrl+Shift+Y` | Toggle extension |

### Content Scripts

This extension injects content scripts into web pages. The content script:

- Runs on specific websites (configured in manifest.json)
- Can interact with page content
- Communicates with the background script

## Configuration

### Permissions

This extension requests the following permissions:

| Permission | Description |
|------------|-------------|
| `storage` | Store user settings |
| `activeTab` | Access current tab |
| `tabs` | Manage browser tabs |

### Options Page

Configure the extension through the options page:

1. Right-click the extension icon
2. Select "Options"
3. Configure your preferences

### Settings

| Setting | Description | Default |
|---------|-------------|---------|
| `theme` | UI theme | `light` |
| `notifications` | Enable notifications | `true` |
| `autoStart` | Start with browser | `false` |

## Development

### Prerequisites

- Node.js 18 or higher
- npm, yarn, or pnpm
- Google Chrome

### Setup

```bash
# Clone the repository
git clone https://github.com/{owner}/{repo}.git
cd {repo}

# Install dependencies
npm install

# Build for development
npm run dev

# Build for production
npm run build
```

### Loading Unpacked Extension

1. Build the extension:
   ```bash
   npm run build
   ```

2. Open Chrome and go to `chrome://extensions/`

3. Enable "Developer mode"

4. Click "Load unpacked"

5. Select the `dist` folder

### Project Structure

```
src/
├── background/      # Background service worker
├── content/         # Content scripts
├── popup/           # Popup UI
├── options/         # Options page
├── components/      # Reusable UI components
├── utils/           # Utility functions
└── types/           # TypeScript types
public/
├── icons/           # Extension icons
└── manifest.json    # Extension manifest
```

### Scripts

```bash
# Development build with watch
npm run dev

# Production build
npm run build

# Run tests
npm test

# Lint code
npm run lint

# Format code
npm run format
```

### Manifest Version

This extension uses Manifest V3:

```json
{
  "manifest_version": 3,
  "name": "My Extension",
  "version": "1.0.0",
  "description": "A Chrome extension for {description}",
  "permissions": ["storage", "activeTab"],
  "background": {
    "service_worker": "background.js"
  },
  "content_scripts": [
    {
      "matches": ["<all_urls>"],
      "js": ["content.js"]
    }
  ],
  "action": {
    "default_popup": "popup.html",
    "default_icon": {
      "16": "icons/icon16.png",
      "48": "icons/icon48.png",
      "128": "icons/icon128.png"
    }
  }
}
```

## Architecture

### Background Script

The background script runs in the background and handles:

- Extension lifecycle events
- Message passing with content scripts
- API calls
- Storage management

### Content Script

The content script runs in the context of web pages and can:

- Read and modify page content
- Interact with the DOM
- Communicate with the background script

### Popup

The popup UI appears when clicking the extension icon and provides:

- Quick actions
- Status information
- Settings access

### Options Page

The options page allows users to configure:

- Extension settings
- Personal preferences
- Advanced options

## Testing

### Running Tests

```bash
# Run all tests
npm test

# Run with coverage
npm run test:coverage

# Run in watch mode
npm run test:watch
```

### Test Structure

```typescript
import { background } from '../src/background';

describe('Background Script', () => {
  it('handles messages', async () => {
    const message = { type: 'GET_DATA' };
    const response = await background.handleMessage(message);
    expect(response.success).toBe(true);
  });
});
```

## Publishing

### Chrome Web Store

1. Build for production:
   ```bash
   npm run build
   ```

2. Create a zip file:
   ```bash
   cd dist && zip -r ../my-extension.zip . && cd ..
   ```

3. Go to the [Chrome Developer Dashboard](https://chrome.google.com/webstore/devconsole)

4. Click "New Item"

5. Upload the zip file

6. Fill in the listing details

7. Submit for review

### Versioning

Follow semantic versioning:

- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT — see [LICENSE](LICENSE) for details.
```

### manifest.json

```json
{
  "manifest_version": 3,
  "name": "My Extension",
  "version": "1.0.0",
  "description": "A Chrome extension for {description}",
  "permissions": [
    "storage",
    "activeTab",
    "tabs"
  ],
  "background": {
    "service_worker": "background.js"
  },
  "content_scripts": [
    {
      "matches": ["<all_urls>"],
      "js": ["content.js"],
      "css": ["content.css"]
    }
  ],
  "action": {
    "default_popup": "popup.html",
    "default_icon": {
      "16": "icons/icon16.png",
      "48": "icons/icon48.png",
      "128": "icons/icon128.png"
    }
  },
  "options_page": "options.html",
  "icons": {
    "16": "icons/icon16.png",
    "48": "icons/icon48.png",
    "128": "icons/icon128.png"
  }
}
```

### package.json

```json
{
  "name": "my-chrome-extension",
  "version": "1.0.0",
  "description": "A Chrome extension for {description}",
  "scripts": {
    "dev": "webpack --watch --mode development",
    "build": "webpack --mode production",
    "test": "vitest",
    "test:coverage": "vitest --coverage",
    "test:watch": "vitest --watch",
    "lint": "eslint src/ --ext .ts",
    "lint:fix": "eslint src/ --ext .ts --fix",
    "format": "prettier --write \"src/**/*.ts\"",
    "format:check": "prettier --check \"src/**/*.ts\"",
    "type-check": "tsc --noEmit",
    "zip": "cd dist && zip -r ../my-extension.zip . && cd .."
  },
  "keywords": [
    "chrome-extension",
    "browser-extension"
  ],
  "author": "{author}",
  "license": "MIT",
  "devDependencies": {
    "@types/chrome": "^0.0.260",
    "@types/node": "^20.10.0",
    "copy-webpack-plugin": "^12.0.0",
    "css-loader": "^6.8.0",
    "eslint": "^8.55.0",
    "html-webpack-plugin": "^5.6.0",
    "prettier": "^3.1.0",
    "style-loader": "^3.3.0",
    "ts-loader": "^9.5.0",
    "typescript": "^5.3.0",
    "vitest": "^1.1.0",
    "webpack": "^5.89.0",
    "webpack-cli": "^5.1.0"
  },
  "engines": {
    "node": ">=18"
  }
}
```

### webpack.config.js

```javascript
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CopyWebpackPlugin = require('copy-webpack-plugin');

module.exports = {
  entry: {
    background: './src/background/index.ts',
    content: './src/content/index.ts',
    popup: './src/popup/popup.ts',
    options: './src/options/options.ts',
  },
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: '[name].js',
  },
  resolve: {
    extensions: ['.ts', '.js'],
  },
  module: {
    rules: [
      {
        test: /\.ts$/,
        use: 'ts-loader',
        exclude: /node_modules/,
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader'],
      },
    ],
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './src/popup/popup.html',
      filename: 'popup.html',
      chunks: ['popup'],
    }),
    new HtmlWebpackPlugin({
      template: './src/options/options.html',
      filename: 'options.html',
      chunks: ['options'],
    }),
    new CopyWebpackPlugin({
      patterns: [
        { from: 'public/manifest.json', to: 'manifest.json' },
        { from: 'public/icons', to: 'icons' },
      ],
    }),
  ],
};
```

### .github/workflows/ci.yml

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Lint
        run: npm run lint
      
      - name: Format check
        run: npm run format:check
      
      - name: Type check
        run: npm run type-check
      
      - name: Test
        run: npm run test:coverage
      
      - name: Build
        run: npm run build
```

## Checklist

When using contributor-ready with a Chrome extension project:

- [ ] Detect Chrome extension type
- [ ] Check manifest.json
- [ ] Check for proper permissions
- [ ] Check for content scripts
- [ ] Check for background script
- [ ] Check for popup UI
- [ ] Generate Chrome extension-specific README
- [ ] Generate Chrome extension-specific CONTRIBUTING.md
- [ ] Generate Chrome extension-specific CI workflow
- [ ] Generate Chrome extension-specific SECURITY.md
- [ ] Generate extension documentation
