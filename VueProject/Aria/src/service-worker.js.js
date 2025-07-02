import { precacheAndRoute } from 'workbox-precaching'

precacheAndRoute(self.__WB_MANIFEST || [])

self.addEventListener('push', (event) => {
  let data = {}

  try {
    data = event.data.json()
  } catch (e) {
    data = {
      title: 'اعلان جدید',
      body: event.data?.text() || '',
      icon: '/img/ali.png',
      badge: '/img/ali.png',
      url: '/'
    }
  }

  const title = data.title || 'اعلان جدید'
  const options = {
    body: data.body || '',
    icon: data.icon || '/img/ali.png',
    badge: data.badge || '/img/ali.png',
    data: { url: data.url || '/' },
    vibrate: [100, 50, 100],
  }

  event.waitUntil(
    self.registration.showNotification(title, options)
  )
})

self.addEventListener('notificationclick', (event) => {
  event.notification.close()
  const urlToOpen = event.notification.data?.url || '/'

  event.waitUntil(
    clients.matchAll({ type: 'window', includeUncontrolled: true }).then((clientList) => {
      for (const client of clientList) {
        if (client.url === urlToOpen && 'focus' in client) {
          return client.focus()
        }
      }
      if (clients.openWindow) {
        return clients.openWindow(urlToOpen)
      }
    })
  )
})
