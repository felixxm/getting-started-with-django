from django.contrib import admin


class MyAdminSite(admin.AdminSite):
    site_title = "🎉 Staging Django site admin 🎉"
    site_header = "📢 💚 STAGING VERSION! 📢 💚"
