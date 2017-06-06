# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1496754418.443604
_enable_loop = True
_template_filename = '/home/ben/OL-blog/lib/python3.5/site-packages/nikola/data/themes/base/templates/index.tmpl'
_template_uri = 'index.tmpl'
_source_encoding = 'utf-8'
_exports = ['content', 'extra_head', 'content_header']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('math', context._clean_inheritance_tokens(), templateuri='math_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'math')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='index_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('pagination', context._clean_inheritance_tokens(), templateuri='pagination_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pagination')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        comments = _mako_get_namespace(context, 'comments')
        prevlink = context.get('prevlink', UNDEFINED)
        prev_next_links_reversed = context.get('prev_next_links_reversed', UNDEFINED)
        current_page = context.get('current_page', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        page_links = context.get('page_links', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        math = _mako_get_namespace(context, 'math')
        posts = context.get('posts', UNDEFINED)
        pagekind = context.get('pagekind', UNDEFINED)
        def content_header():
            return render_content_header(context._locals(__M_locals))
        pagination = _mako_get_namespace(context, 'pagination')
        front_index_header = context.get('front_index_header', UNDEFINED)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        index_file = context.get('index_file', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        index_teasers = context.get('index_teasers', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        comments = _mako_get_namespace(context, 'comments')
        prevlink = context.get('prevlink', UNDEFINED)
        prev_next_links_reversed = context.get('prev_next_links_reversed', UNDEFINED)
        current_page = context.get('current_page', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        page_links = context.get('page_links', UNDEFINED)
        math = _mako_get_namespace(context, 'math')
        posts = context.get('posts', UNDEFINED)
        def content_header():
            return render_content_header(context)
        pagekind = context.get('pagekind', UNDEFINED)
        pagination = _mako_get_namespace(context, 'pagination')
        front_index_header = context.get('front_index_header', UNDEFINED)
        def content():
            return render_content(context)
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        index_teasers = context.get('index_teasers', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_header'):
            context['self'].content_header(**pageargs)
        

        __M_writer('\n')
        if 'main_index' in pagekind:
            __M_writer('    ')
            __M_writer(str(front_index_header))
            __M_writer('\n')
        if page_links:
            __M_writer('    ')
            __M_writer(str(pagination.page_navigation(current_page, page_links, prevlink, nextlink, prev_next_links_reversed)))
            __M_writer('\n')
        __M_writer('<div class="postindex">\n')
        for post in posts:
            __M_writer('    <article class="h-entry post-')
            __M_writer(str(post.meta('type')))
            __M_writer('">\n    <header>\n        <h1 class="p-name entry-title"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" class="u-url">')
            __M_writer(filters.html_escape(str(post.title())))
            __M_writer('</a></h1>\n        <div class="metadata">\n            <p class="byline author vcard"><span class="byline-name fn" itemprop="author">\n')
            if author_pages_generated:
                __M_writer('                <a href="')
                __M_writer(str(_link('author', post.author())))
                __M_writer('">')
                __M_writer(filters.html_escape(str(post.author())))
                __M_writer('</a>\n')
            else:
                __M_writer('                ')
                __M_writer(filters.html_escape(str(post.author())))
                __M_writer('\n')
            __M_writer('            </span></p>\n            <p class="dateline"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" rel="bookmark"><time class="published dt-published" datetime="')
            __M_writer(str(post.formatted_date('webiso')))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
            __M_writer('">')
            __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
            __M_writer('</time></a></p>\n')
            if not post.meta('nocomments') and site_has_comments:
                __M_writer('                <p class="commentline">')
                __M_writer(str(comments.comment_link(post.permalink(), post._base_path)))
                __M_writer('\n')
            __M_writer('        </div>\n    </header>\n')
            if index_teasers:
                __M_writer('    <div class="p-summary entry-summary">\n    ')
                __M_writer(str(post.text(teaser_only=True)))
                __M_writer('\n')
            else:
                __M_writer('    <div class="e-content entry-content">\n    ')
                __M_writer(str(post.text(teaser_only=False)))
                __M_writer('\n')
            __M_writer('    </div>\n    </article>\n')
        __M_writer('</div>\n')
        __M_writer(str(helper.html_pager()))
        __M_writer('\n')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\n')
        __M_writer(str(math.math_scripts_ifposts(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_head():
            return render_extra_head(context)
        index_file = context.get('index_file', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        math = _mako_get_namespace(context, 'math')
        posts = context.get('posts', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if posts and (permalink == '/' or permalink == '/' + index_file):
            __M_writer('        <link rel="prefetch" href="')
            __M_writer(str(posts[0].permalink()))
            __M_writer('" type="text/html">\n')
        __M_writer('    ')
        __M_writer(str(math.math_styles_ifposts(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_header():
            return render_content_header(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "index.tmpl", "line_map": {"128": 24, "129": 25, "130": 26, "131": 26, "132": 26, "133": 28, "134": 28, "135": 28, "136": 28, "137": 31, "138": 32, "139": 32, "140": 32, "141": 32, "142": 32, "143": 33, "144": 34, "145": 34, "146": 34, "147": 36, "148": 37, "149": 37, "150": 37, "23": 3, "152": 37, "153": 37, "26": 4, "155": 37, "156": 38, "29": 2, "158": 39, "159": 39, "32": 5, "161": 43, "162": 44, "163": 45, "164": 45, "165": 46, "38": 0, "167": 48, "168": 48, "169": 50, "170": 53, "171": 54, "172": 54, "173": 55, "174": 55, "157": 39, "176": 56, "200": 13, "182": 8, "201": 13, "151": 37, "193": 8, "198": 11, "160": 41, "175": 56, "195": 9, "196": 10, "69": 2, "70": 3, "71": 4, "72": 5, "73": 6, "202": 13, "78": 14, "208": 17, "83": 57, "197": 11, "89": 16, "219": 208, "199": 11, "166": 47, "194": 9, "154": 37, "114": 16, "119": 17, "120": 18, "121": 19, "122": 19, "123": 19, "124": 21, "125": 22, "126": 22, "127": 22}, "filename": "/home/ben/OL-blog/lib/python3.5/site-packages/nikola/data/themes/base/templates/index.tmpl", "source_encoding": "utf-8"}
__M_END_METADATA
"""
