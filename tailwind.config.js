/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,jsx}'],
  theme: {
    extend: {
      colors: {
        abyss: '#050505',
        violet: '#6A00FF'
      },
      boxShadow: {
        glow: '0 0 30px rgba(106, 0, 255, 0.35)'
      },
      fontFamily: {
        display: ['Inter', 'system-ui', 'sans-serif']
      }
    }
  },
  plugins: []
};
