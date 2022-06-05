# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/00_wp2md.ipynb (unless otherwise specified).

__all__ = ['url2api', 'WP', 'wp2md']

# Cell
import re
from fastcore.all import urljson, AttrDict, Path, first, test_eq, urlread, urlsave, L, call_parse, store_true, Param
from IPython.display import Markdown
from markdownify import markdownify as md
from json import dumps

# Cell
def _getpost(url:str=None, post_id:int=None, baseurl:str=None):
    if url: post=urljson(url)
    else: post=urljson(f'{baseurl}/{post_id}')
    return AttrDict(post)

# Cell
_re_api = re.compile(r'<link rel="alternate" type="application/json" href="(\S+)"')

def url2api(url):
    "Get the wordpress api endpoint to retrieve post from the public url"
    api = first(_re_api.findall(urlread(url)))
    if not api: raise Exception("Was not able to find Wordpress ID in site.  Pleasure ensure that the URL corresponds to a wordpress site.")
    return api

# Cell

_re_img = re.compile(r'\!\[.*?\]\((\S+)\)')

class WP:
    def __init__(self, url:str=None, baseurl:str=None, post_id:int=None, dest_path:str=None, dest_file:str=None):
        if url:
            self.posturl = url2api(url)
            self.baseurl = self.posturl.split('posts/')[0]
        else:
            self.baseurl = baseurl if baseurl.endswith('/') else baseurl+'/'
            self.posturl = f"{self.baseurl}posts/{post_id}"

        self.post = _getpost(self.posturl)
        self.img_map = {}
        self.dest_path = self.dest_path = '.' if not dest_path else dest_path
        self.dest_file = self.slug+'.md' if not dest_file else dest_file

    _props = ['title', 'date', 'tags', 'keywords', 'draft', 'description', 'image', 'slug']

    @property
    def mdimages(self): return _re_img.findall(self.raw_markdown)

    def save_images(self, dest_path, nb_path):
        for i,img in enumerate(self.mdimages):
            dest=Path(dest_path)/f'{i}_img'
            file_pth = urlsave(img, dest=dest)
            self.img_map[img] = str(file_pth.relative_to(nb_path))
        if getattr(self, 'image'):
            img = self.image
            dest=Path(dest_path)/f'og.png'
            file_pth = urlsave(img, dest=dest)
            self.img_map[img] = str(file_pth.relative_to(nb_path))

    def _replace_images(self, md):
        for o,n in self.img_map.items():
            md = re.sub(o, n, md)
        return md

    @property
    def keywords(self) -> list:
        return self.tags

    @property
    def tags(self) -> list:
        _tags = L(self.post.get('categories')).map(self._tagid2nm).filter()
        return dumps(list(_tags))


    def _tagid2nm(self, id) -> str:
        return urljson(f"{self.baseurl}categories/{id}").get('name')

    @property
    def draft(self) -> str:
        return str(self.post.draft != 'publish').lower()

    @property
    def description(self) -> str:
        return self.post.yoast_head_json.get('description')

    @property
    def title(self) -> str:
        title = self.post.get('title', None)
        return title.get('rendered', None) if title else title

    @property
    def image(self) -> str:
        img = self.post.get('uagb_featured_image_src', None)
        return first(img.get('large', [])) if img else img

    @property
    def frontmatter(self) -> str:
        fm = '---\n'
        for p in self._props:
            attr = getattr(self, p, None)
            if attr:
                if p == 'image': fm+=f'{p}: ./{self.img_dir}/og.png\n'
                elif p not in ['keywords', 'tags']: fm+=f'{p}: "{attr}"\n'
                else: fm+=f'{p}: {attr}\n'
        return fm+'---\n'

    def __getattr__(self, name):
        return self.post.get(name, None)

    @property
    def raw_markdown(self) -> str: return md(self.post.content['rendered'])

    @property
    def markdown(self) -> str:
        "Return the markdown representation of the body of the post."
        return self.frontmatter + self._replace_images(self.raw_markdown)

    @property
    def dest_file_path(self) -> Path: return Path(self.dest_path)/self.dest_file

    @property
    def img_dir(self) -> Path:
        return self.dest_file_path.parent/f'_{self.dest_file_path.stem}_data'

    def tomd(self, download=True) -> None:
        "Write markdown representation of wordpress post"
        if download: self.save_images(self.img_dir, nb_path=self.dest_path)
        print(f'Writing: {self.dest_file_path}')
        self.dest_file_path.write_text(self.markdown)

# Cell
@call_parse
def wp2md(url_or_id:Param('the public URL of the WP article OR the post id', str),
          apiurl:Param('the base url for the wordpress api to retrieve posts for your site.', str)='https://outerbounds.com/wp-json/wp/v2/posts',
          dest_path:Param('The path to save the markdown file to', str)='.',
          dest_file:Param('Name of destination markdown file. If not given defaults to the slug indicated in wordpress', str)=None,
          no_download:Param('Pass this flag to NOT download any images locally', store_true)=False,
         ):
    "Convert A wordpress post into markdown file with front matter."
    if url_or_id.isnumeric(): post = WP(baseurl=apiurl, post_id=url_or_id)
    else: post = WP(url=url_or_id, dest_path=dest_path, dest_file=dest_file)
    post.tomd(download=not no_download)