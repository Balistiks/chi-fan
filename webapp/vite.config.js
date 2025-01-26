import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig(() => {
  return {
    build: {
      outDir: 'build',
    },
    plugins: [react()],
    define: {
      'process.env.SECRET_TOKEN': JSON.stringify(process.env.SECRET_TOKEN),
      'proccess.env.URL': JSON.stringify(process.env.URL)
    },
    server: {
      host: true,
      port: 8081
    }
  };
});
