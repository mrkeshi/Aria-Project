import { fileURLToPath, URL } from 'node:url'
import { VitePWA } from 'vite-plugin-pwa'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [
    VitePWA({
      registerType: 'autoUpdate',
    


      workbox: {
        maximumFileSizeToCacheInBytes: 5 * 1024 * 1024,
        runtimeCaching: [
   
        ],
      },      
      manifest: {
        name: 'Aria',
        short_name: 'Aria',
        start_url: '/',
        display: 'standalone',
        background_color: '#ffffff',
        theme_color: '#2563eb',
        icons: [
          {
            src: 'img/ali.png',
            sizes: '192x192',
            type: 'image/png',
          },
          {
            src: 'img/ali.png',
            sizes: '512x512',
            type: 'image/png',
          },
        ],
      },
    }),
  ,
    vue(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})
