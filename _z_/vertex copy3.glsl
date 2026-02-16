void main() {
    vec4 doc_pos = $visual_to_doc(vec4($position, 0, 1));
    vec4 adjusted;
    if ($adjust_dir.x == 0.0) {
        adjusted = doc_pos;
    } else {
        vec4 doc_x = 
            $visual_to_doc(vec4($adjust_dir.x, 0, 0, 0)) -
            $visual_to_doc(vec4(0, 0, 0, 0));
        vec4 doc_y = 
            $visual_to_doc(vec4(0, $adjust_dir.y, 0, 0)) -
            $visual_to_doc(vec4(0, 0, 0, 0));
        doc_x = normalize(doc_x);
        doc_y = normalize(doc_y);
        vec4 proj_y_x = dot(doc_x, doc_y) * doc_x;
        float cur_width = length(doc_y - proj_y_x);
        adjusted = doc_pos + ($line_width / cur_width) * (doc_x + doc_y);
    }

    gl_Position = $doc_to_render(adjusted);
}