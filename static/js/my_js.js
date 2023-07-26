function sendComment(blogId) {
    const comment = $('#comment').val();
    const parentId = $('#parent_id').val();
    $.get('/blog/send-comment', {
        blog_comment: comment,
        blog_id: blogId,
        parent_id: parentId
    }).then(res => {
        $('#comments-region').html(res);
        $('#comment').val('');
        $('#parent_id').val('');
        if (parentId !== '') {
            document.getElementById('comment-pointer').scrollIntoView({behavior: "smooth"});
        } else {
            document.getElementById('comments-region').scrollIntoView({behavior: "smooth"});
        }
    });
}

function replyComment(parentId) {
    $('#parent_id').val(parentId);
    document.getElementById('comment_answer').scrollIntoView({behavior: "smooth"});
}
