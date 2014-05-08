from django.db import models
from django.template.defaultfilters import slugify
from settings import SITE_ROOT
import os.path




class MediaNode(models.Model):
	title = models.CharField(max_length=600,blank=True)
	description = models.CharField(max_length=300, blank=True)
	link = models.URLField(max_length=1000, blank=True,help_text="For links to external sites; used for 'Client Images', and links to websites");
	vimeo = models.CharField(max_length=1000, blank=True,help_text="This is only used for Presentation Pages (submitting for competition links), the link should look like 'http://vimeo.com/85560958' . Be sure to also add a image, it will be show before playing the video. ");
	order = models.IntegerField(blank=True,default=99)

	def slugify_filename(instance, filename):
		fname, dot, extension = filename.rpartition('.')
		slug = slugify(fname)
		instance.title = '%s.%s' % (slug, extension)
		return '%s.%s' % (slug, extension)

	location = models.FileField(upload_to=slugify_filename)
	location.verbose_name=u'Uploaded element'
	def save(self, *args, **kwargs):
		fname, dot, extension = os.path.basename(self.location.name).rpartition('.')
		fname = slugify(fname)
		self.title = '%s.%s'%(fname,extension)
		super(MediaNode, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title

	def admin_image(self):
		if self.title:
			return '<img style="width:200px;height:auto;" src="http://also-static.com/dotdotdash/uploaded/%s"/>' % self.title
		return "not an image"
	admin_image.allow_tags = True

	def admin_video(self):
		if self.video:
			return '<iframe src="%s?title=0&amp;byline=0&amp;portrait=0&amp;color=ff0179;autoplay=1" width="500" height="281" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>' % self.video
		return "not an video"
	admin_video.allow_tags = True




class Home(models.Model):
	class Meta:
		verbose_name = 'Quotes & Video'
	quote1 = models.TextField(max_length=1000)
	quote2 = models.TextField(max_length=1000)

	mp4 = models.ForeignKey(MediaNode,blank=True,null=True,related_name="mp4+")
	ogv = models.ForeignKey(MediaNode,blank=True,null=True,related_name="ogv+")
	webm = models.ForeignKey(MediaNode,blank=True,null=True,related_name="webm+")
	workbackgroundimage = models.ForeignKey(MediaNode,blank=True,null=True,related_name="bkimg+")
	youtubeId = models.CharField(max_length=100,blank=True,help_text='Should look something like "1PxQj_HiQjo"')
	quote3 = models.TextField(max_length=1000)
	quote4 = models.TextField(max_length=1000)

	def bk_image(self):
		if self.workbackgroundimage:
			return '<img style="width:200px;height:auto;" src="http://also-static.com/dotdotdash/uploaded/%s"/>' % self.workbackgroundimage
		return "not an image"
	bk_image.allow_tags = True
	bk_image.short_description = "Selected Image"


class About(models.Model):
	class Meta:
		verbose_name_plural = "About"
	about =	models.TextField(max_length=4000)
	process = models.TextField(max_length=4000)
	backgroundimage = models.ForeignKey(MediaNode,blank=True,null=True,related_name="bkimg+")

	def admin_image(self):
		if self.backgroundimage:
			return '<img style="width:200px;height:auto;" src="http://also-static.com/dotdotdash/uploaded/%s"/>' % self.backgroundimage
		return "not an image"
	admin_image.allow_tags = True
	admin_image.short_description = "Selected Image"

class Services(models.Model):
	class Meta:
		verbose_name_plural = "Services"
	services = models.TextField(max_length=2000)

	socialmediastrategyplanning = models.TextField(max_length=2000)
	branding = models.TextField(max_length=2000)
	research = models.TextField(max_length=2000)

	creativedevelopment = models.TextField(max_length=2000)
	contentproduction = models.TextField(max_length=2000)
	resultsanalytics = models.TextField(max_length=2000)

	backgroundimage = models.ForeignKey(MediaNode,blank=True,null=True,related_name="bkimg+")
	backgroundimage.short_description = 'Social media'
	backgroundimage.verbose_name=u'Social media'
	def bk_image(self):
		if self.backgroundimage:
			return '<img style="width:200px;height:auto;" src="http://also-static.com/dotdotdash/uploaded/%s"/>' % self.backgroundimage
		return "not an image"
	bk_image.allow_tags = True
	bk_image.short_description = "Selected Image"

	socimage = models.ForeignKey(MediaNode,blank=True,null=True,related_name="1img+")
	def soc_image(self):
		if self.backgroundimage:
			return '<img style="width:200px;height:auto;" src="http://also-static.com/dotdotdash/uploaded/%s"/>' % self.socimage
		return "not an image"
	soc_image.allow_tags = True
	soc_image.short_description = "Selected Image"

	brandingimage = models.ForeignKey(MediaNode,blank=True,null=True,related_name="2img+")
	def brandingimage_image(self):
		if self.backgroundimage:
			return '<img style="width:200px;height:auto;" src="http://also-static.com/dotdotdash/uploaded/%s"/>' % self.brandingimage
		return "not an image"
	brandingimage_image.allow_tags = True
	brandingimage_image.short_description = "Selected Image"

	researchimage = models.ForeignKey(MediaNode,blank=True,null=True,related_name="3img+")
	def researchimage_image(self):
		if self.backgroundimage:
			return '<img style="width:200px;height:auto;" src="http://also-static.com/dotdotdash/uploaded/%s"/>' % self.researchimage
		return "not an image"
	researchimage_image.allow_tags = True
	researchimage_image.short_description = "Selected Image"

	creativedevimage = models.ForeignKey(MediaNode,blank=True,null=True,related_name="4img+")
	def creativedevimage_image(self):
		if self.backgroundimage:
			return '<img style="width:200px;height:auto;" src="http://also-static.com/dotdotdash/uploaded/%s"/>' % self.creativedevimage
		return "not an image"
	creativedevimage_image.allow_tags = True
	creativedevimage_image.short_description = "Selected Image"

	contentproductionimage = models.ForeignKey(MediaNode,blank=True,null=True,related_name="5img+")
	def contentproductionimage_image(self):
		if self.backgroundimage:
			return '<img style="width:200px;height:auto;" src="http://also-static.com/dotdotdash/uploaded/%s"/>' % self.contentproductionimage
		return "not an image"
	contentproductionimage_image.allow_tags = True
	contentproductionimage_image.short_description = "Selected Image"

	resultsimage = models.ForeignKey(MediaNode,blank=True,null=True,related_name="6img+")
	def resultsimage_image(self):
		if self.backgroundimage:
			return '<img style="width:200px;height:auto;" src="http://also-static.com/dotdotdash/uploaded/%s"/>' % self.resultsimage
		return "not an image"
	resultsimage_image.allow_tags = True
	resultsimage_image.short_description = "Selected Image"


class Clients(models.Model):
	class Meta:
		verbose_name_plural = "Clients"
	text = models.TextField(max_length=2000)
	clientimages = models.ManyToManyField(MediaNode,blank=True,related_name="imageFields+")
	backgroundimage = models.ForeignKey(MediaNode,blank=True,null=True,related_name="bkimg+")

	def bk_image(self):
		if self.backgroundimage:
			return '<img style="width:200px;height:auto;" src="http://also-static.com/dotdotdash/uploaded/%s"/>' % self.backgroundimage
		return "not an image"
	bk_image.allow_tags = True
	bk_image.short_description = "Selected Image"

	def allClients(self):
		out = "<div style='text-align:center;'><br>"
		if self.clientimages:
			for img in self.clientimages.order_by("order").all():
				out += '<a href="/admin/dotdotdash/medianode/%s/" target="_blank" style="text-align:left;display:inline-block; padding:1em; border:1px solid #eee"><label style="float:none;width:auto;font-weight: bold !important;color: #333 !important;">title: %s<br>link: %s<br>order: %s</label> <img style="width:200px;height:auto;" src="http://also-static.com/dotdotdash/uploaded/%s"/><br></a>' % (img.id,img,img.link,img.order,img)
		out += "</div>"
		return out
	allClients.allow_tags = True
	allClients.short_description = "Selected Clients"

class Page(models.Model):
	class Meta:
		verbose_name_plural = "Slides (for Projects)"
		ordering = ['order']
	pageTypes = (
		("text","text"),
		("singleImage","singleImage"),
		("fourImage","fourImage"),
		("imageWText","imageWText"),
		("pdf","pdf"),
		("linktoexternal","linktoexternal"),
		("singleImageNoStrech","singleImageNoStrech")
	)
	title = models.CharField(max_length=600)
	textFields = models.TextField(max_length=1000,blank=True)
	mediaField = models.ManyToManyField(MediaNode,blank=True,related_name="images+")
	videoURL = models.URLField(max_length=800, blank=True)
	pageType = models.CharField(max_length=30, choices=pageTypes)
	slug = models.SlugField(blank=True)
	order = models.IntegerField(blank=True,default=99)
	pdf = models.ManyToManyField(MediaNode,blank=True,related_name="pdf+")
	project = models.CharField(max_length=400,blank=True,default="not defined")
	def save(self,*args, **kwargs):
		self.slug = slugify(self.title)
		super(Page, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title

class Work(models.Model):
	class Meta:
		verbose_name = 'Project'
	title = models.CharField(max_length=600)
	subTitle = models.CharField(max_length=600)
	pages = models.ManyToManyField(Page,blank=True,related_name="pages+")
	description = models.TextField(max_length=1000)
	datefororder = models.DateField(auto_now=True)
	slug = models.SlugField(blank=True)
	order = models.IntegerField(blank=True,default=99)
	is_a_sos_project = models.BooleanField(blank=True,default=False)
	image = models.ManyToManyField(MediaNode,blank=True)

	def save(self,*args, **kwargs):
		self.slug = slugify(self.title)
		super(Work, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title

class Contact(models.Model):
	class Meta:
		verbose_name_plural = "Contact"
	contant = models.TextField(max_length=4000)
	backgroundimage = models.ForeignKey(MediaNode,blank=True,null=True,related_name="bkimg+")
	def admin_image(self):
		if self.backgroundimage:
			return '<img style="width:200px;height:auto;" src="http://also-static.com/dotdotdash/uploaded/%s"/>' % self.backgroundimage
		return "not an image"
	admin_image.allow_tags = True
	admin_image.short_description=u'BackgroundImage'

class Project(models.Model):
	class Meta:
		verbose_name = 'Presentation Project'
	title = models.CharField(max_length=600)
	slug = models.SlugField(blank=True)
	clientimages = models.ManyToManyField(MediaNode)
	order = models.IntegerField(default=99, blank=True)
	clientimages.verbose_name = "Included media"

	def save(self,*args, **kwargs):
		self.slug = slugify(self.title)
		super(Project, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title

class PersonalizedPage(models.Model):
	class Meta:
		verbose_name = 'Presentation Page'
	title = models.CharField(max_length=600)
	slug = models.SlugField(blank=True,verbose_name="link")
	textBlock = models.TextField(max_length=4000, blank=True)
	projects = models.ManyToManyField(Project)

	def save(self,*args, **kwargs):
		self.slug = slugify(self.title)
		super(PersonalizedPage, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title
