function CodeBlock(el)
  if el.classes[1] == 'mermaid' then
    -- Write the mermaid code to a temporary file
    local temp_mmd = 'temp.mmd'
    local f_mmd = io.open(temp_mmd, 'w')
    f_mmd:write(el.text)
    f_mmd:close()

    -- Run mmdc to convert the file to svg
    local temp_svg = 'temp.svg'
    os.execute('mmdc -i ' .. temp_mmd .. ' -o ' .. temp_svg)

    -- Read the svg content
    local f_svg = io.open(temp_svg, 'r')
    local svg_content = f_svg:read('*a')
    f_svg:close()

    -- Clean up temporary files
    os.remove(temp_mmd)
    os.remove(temp_svg)

    -- Return the svg content as a RawBlock
    return pandoc.RawBlock('html', svg_content)
  end
end
