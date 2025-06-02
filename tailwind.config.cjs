import type { Config } from 'tailwindcss';
import flowbitePlugin from 'flowbite/plugin'

export default {
  content: ['./src/**/*.{html,js,svelte,ts}', './node_modules/flowbite-svelte/**/*.{html,js,svelte,ts}'],
  darkMode: 'selector',
  theme: {
    extend: {
      colors: {
        // flowbite-svelte
        primary: {
          50: '#ffffff',
          100: '#ccf0e9',
          200: '#00b48f',
          300: '#80d9c7',
          400: '#007c57',
          500: '#00694b',
          600: '#124231',
          700: '#F49F49',
          800: 'black',
          900: '#000000'
        },
        named: {
          white: 'white',
          soft_green: '#ccf0e9',
          pale_green: '#00b48f',
          light_green: '#80d9c7',
          medium_green: '#007c57',
          dark_green: '#00694b',
          inky_green: '#124231',
          heavy_green: '#144835',
          orange_highlight: '#F49F49',
          nav_hf_background: '#3A3B3C',
          black: 'black'
        },
        gray: {
          lightest: '#d7d7d7',
          light: 'rgb(138, 138, 138)',
          medium: 'rgb(98, 98, 98)',
          dark: 'rgb(59, 59, 59)',
          darkest: '#1b1b1b',
        }
      }
    }
  },
  // },
  plugins: [
    flowbitePlugin,
    function ({ addBase, theme }) {
      addBase({
        ':root': {
          '--primary-50': theme('colors.primary.50'),
          '--primary-100': theme('colors.primary.100'),
          '--primary-200': theme('colors.primary.200'),
          '--primary-300': theme('colors.primary.300'),
          '--primary-400': theme('colors.primary.400'),
          '--primary-500': theme('colors.primary.500'),
          '--primary-600': theme('colors.primary.600'),
          '--primary-700': theme('colors.primary.700'),
          '--primary-800': theme('colors.primary.800'),
          '--primary-900': theme('colors.primary.900'),
          '--named-white': theme('colors.named.white'),
          '--named-soft_green': theme('colors.named.soft_green'),
          '--named-pale_green': theme('colors.named.pale_green'),
          '--named-light_green': theme('colors.named.light_green'),
          '--named-medium_green': theme('colors.named.medium_green'),
          '--named-dark_green': theme('colors.named.dark_green'),
          '--named-inky_green': theme('colors.named.inky_green'),
          '--named-heavy_green': theme('colors.named.heavy_green'),
          '--named-orange_highlight': theme('colors.named.orange_highlight'),
          '--named-nav_hf_background': theme('colors.named.nav_hf_background'),
          '--named-black': theme('colors.named.black'),
          '--gray_scale-lightest': theme('colors.gray_scale.lightest'),
          '--gray_scale-light': theme('colors.gray_scale.light'),
          '--gray_scale-medium': theme('colors.gray_scale.medium'),
          '--gray_scale-dark': theme('colors.gray_scale.dark'),
          '--gray_scale-darkest': theme('colors.gray_scale.darkest'),
        },
      });
    },
  ]
} as Config;