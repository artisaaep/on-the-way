import {vitePreprocess} from "@sveltejs/vite-plugin-svelte";
import adapter from '@sveltejs/adapter-static';

const dev = 'development' === process.env.NODE_ENV;
const base = dev ? '' : '/app';

/** @type {import('@sveltejs/kit').Config} */
const config = {
  kit: {
    adapter: adapter(),
    paths: {
      base,
    },
  },
  preprocess: vitePreprocess(),
  vitePlugin: {
    // This enables compile-time warnings to be
    // visible in the learn.svelte.dev editor
  },

};

export default config;
