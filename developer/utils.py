class PostMixin:
    lesson_attr = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object_list[0]
        context['title'] = post.lesson
        context['posts'] = post
        if self.lesson_attr:
            context['lesson'] = getattr(post, self.lesson_attr).all().order_by('pk')
        return context
