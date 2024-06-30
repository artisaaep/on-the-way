import { nodeResolve } from '@rollup/plugin-node-resolve';
import commonjs from '@rollup/plugin-commonjs';
import terser from '@rollup/plugin-terser';
import typescript from '@rollup/plugin-typescript';

export default [
    {
        input: 'scripts/comic.ts',
        output: {
            file: 'dest/comic.js',
            format: 'esm'
        },
        plugins: [commonjs(), nodeResolve({ browser: true }), typescript(), terser()],
    },
    {
        input: 'scripts/script.ts',
        output: {
            file: 'dest/script.js',
            format: 'esm'
        },
        plugins: [commonjs(), nodeResolve({ browser: true }), typescript(), terser()],
    }
];