const content_to_merge = [docs[i].content, docs[i].mt_alt_names];
docs[i].content = content_to_merge.join(' ');
