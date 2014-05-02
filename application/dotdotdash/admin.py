from django.contrib import admin
from dotdotdash.models import *

class mediaAdmin(admin.ModelAdmin):
	list_display = ('title','admin_image')
	readonly_fields = ["admin_image",]
	search_fields = ('title', )
	fieldsets = [
		(None,{'fields':[('location',"admin_image")]}),
		('Advance options', {
			'fields':('link','order','vimeo','description'),
			}),
	]

class HomeAdmin(admin.ModelAdmin):
	readonly_fields=['bk_image',]
	fieldsets = [
		("Quotes",{'fields':['quote1','quote2',"quote3","quote4"]}),
		("Video",{'fields':[('workbackgroundimage','bk_image'),'youtubeId']})
	]

class ClientsAdmin(admin.ModelAdmin):
	filter_horizontal = ("clientimages",)
	readonly_fields = ["allClients",]
	fieldsets= [
		(None,{'fields':['text','clientimages','allClients']})
	]

class ContactAdmin(admin.ModelAdmin):
	readonly_fields=['admin_image',]
	fieldsets = [(None,{'fields':['contant',('backgroundimage','admin_image')]})]

class AboutAdmin(admin.ModelAdmin):
	readonly_fields= ["admin_image",]
	fieldsets= [
		(None,{'fields':['about','process',('backgroundimage','admin_image')]})
	]

class ServicesAdmin(admin.ModelAdmin):
	readonly_fields = [
		"bk_image",
		"soc_image",
		"brandingimage_image",
		"researchimage_image",
		"creativedevimage_image",
		"contentproductionimage_image",
		"resultsimage_image",
	]
	fieldsets = [
		(None,{	'fields':
			[
				"services",
				"socialmediastrategyplanning",
				"branding",
				"research",
				"creativedevelopment",
				"contentproduction",
				"resultsanalytics",
				"backgroundimage",
				"bk_image",
				"socimage",
				"soc_image",
				"brandingimage",
				"brandingimage_image",
				"researchimage",
				"researchimage_image",
				"creativedevimage",
				"creativedevimage_image",
				"contentproductionimage",
				"contentproductionimage_image",
				"resultsimage",
				"resultsimage_image",
			]})
	]

admin.site.register(Home,HomeAdmin)
admin.site.register(About,AboutAdmin)
admin.site.register(Services,ServicesAdmin)
admin.site.register(Clients,ClientsAdmin)
admin.site.register(Contact,ContactAdmin)

class pageAdmin(admin.ModelAdmin):
	def get_model_perms(self, request):
		return {}
	list_display = ('title','project','order','pageType')
	filter_horizontal = ("mediaField",)
	list_filter = ('project', )

	fieldsets = [
		(None,{'fields':['title','project','mediaField',("pageType","order")]}),

		('Viemo',{
			'description':("Add the Viemo url(from the embeded method) here it should look something like this... http://player.vimeo.com/video/52542094?title=0&amp;byline=0&amp;portrait=0&amp;color=ff0179"),
			'fields':['videoURL'],
			}),
		("PDF",{
			'description':("Upload the pdf here, and a jpg of the PDF in the mediaField"),
			'fields':['pdf'],
			}),
		("Text",{
			'description':("This text will be displayed when the proper pageType"),
			'fields':['textFields'],
			}),
	]

class workInline(admin.TabularInline):
	model = Work.pages.through
	extra = 0
	readonly_fields = ['changeform_link','orderObject',]
	def changeform_link(self,instance):
		if instance.id:
			return u'<a href="/admin/dotdotdash/page/%s/" target="_blank">Edit</a>' % (instance.page_id)
		return u'The link is not available till after we save'
	changeform_link.allow_tags = True
	changeform_link.short_description = 'Link'

	def orderObject(self,instance):
		if instance.page_id:
			curPage = Page.objects.get(id=instance.page_id)
			if(not curPage):
				return "not object found"
			return curPage.order
	orderObject.allow_tags = True
	orderObject.short_description="Order"

	verbose_name = "Page"
	verbose_name_plural = "Pages"


class workAdmin(admin.ModelAdmin):
	list_display = ('title','order')
	filter_horizontal = ("image",)
	inlines = [ workInline, ]
	fieldsets = [(None,{'fields':[("title","subTitle","order"),"image"]})]




admin.site.register(MediaNode,mediaAdmin)
admin.site.register(Work,workAdmin)
admin.site.register(Page,pageAdmin)





class ProjectAdmin(admin.ModelAdmin):
	def get_model_perms(self, request):
		return {}
	filter_horizontal = ("clientimages",)
	list_display = ('title','order')
	fieldsets = [(None,{'fields':[('title','order'),'clientimages','slug']})]

class ProjectsInline(admin.TabularInline):
	model = PersonalizedPage.projects.through
	extra = 0
	readonly_fields = ['changeform_link', 'orderObject',]
	def changeform_link(self,instance):
		if instance.project_id:
			return u'<a href="/admin/dotdotdash/project/%s/" target="_blank">Edit</a>' % instance.project_id
		return u'The link is not available till after we save'
	changeform_link.allow_tags = True
	changeform_link.short_description = 'Link'

	def orderObject(self,instance):
		if instance.project_id:
			curPage = Project.objects.get(id=instance.project_id)
			if(not curPage):
				return "not object found"
			return curPage.order
	orderObject.allow_tags = True
	orderObject.short_description="Order"

	verbose_name = "Project"

class PersonalizedPageInlineAdmin(admin.ModelAdmin):
	model = PersonalizedPage
	inlines = [ ProjectsInline, ]
	fieldsets = [(None,{'fields':[("title","slug",),"textBlock"]})]
	readonly_fields = ["slug"]

admin.site.register(Project,ProjectAdmin)
admin.site.register(PersonalizedPage,PersonalizedPageInlineAdmin)

