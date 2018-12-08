$('#file-upload1').change(function() {
    var i = $(this).prev('label').clone();
    var file = $('#file-upload1')[0].files[0].name;
    $(this).prev('label').text(file);
});

$('#file-upload2').change(function() {
    var i = $(this).prev('label').clone();
    var file = $('#file-upload2')[0].files[0].name;
    $(this).prev('label').text(file);
});