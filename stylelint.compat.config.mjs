import official from 'stylelint-config-obsidianmd';

// Focused compatibility audit. This is not a replacement for the complete
// marketplace review or the official config's formatting rules.
const rules = Object.fromEntries(
    Object.entries(official.rules).filter(([name]) => [
        'plugin/no-unsupported-browser-features',
        'selector-type-no-unknown',
        'declaration-no-important',
    ].includes(name)),
);

export default {
    plugins: official.plugins,
    rules: {
        ...rules,
        'plugin/no-unsupported-browser-features': [true, {
            ...official.rules['plugin/no-unsupported-browser-features'][1],
            // Measured in our Obsidian 1.13.7 installation: Electron 39.8.3.
            browsers: ['electron >= 39'],
        }],
        'selector-type-no-unknown': [true, {
            severity: 'warning',
            // Actual MathJax output, not misspelled HTML elements.
            ignoreTypes: ['mjx-stretchy-h', 'mjx-ext'],
        }],
    },
};
