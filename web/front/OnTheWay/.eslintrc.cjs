module.exports = {
  root: true,
  env: {
    browser: true,
    es2021: true,
  },
  extends: [
    'eslint:recommended',
    'plugin:@typescript-eslint/recommended',
    'plugin:svelte/recommended',
  ],
  parser: '@typescript-eslint/parser',
  parserOptions: {
    ecmaVersion: 2021,
    sourceType: 'module',
    extraFileExtensions: ['.svelte'],
  },
  plugins: ['@typescript-eslint', 'svelte'],
  overrides: [
    {
      files: ['*.svelte'],
      parser: 'svelte-eslint-parser',
      parserOptions: {
        parser: '@typescript-eslint/parser',
        project: './tsconfig.json',
      },
    },
  ],
  settings: {
    'svelte3/typescript': () => require('typescript'),
  },
  ignorePatterns: ['node_modules/', 'build', '.svelte-kit', 'dist'],
};
