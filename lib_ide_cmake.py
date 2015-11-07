# BuildFox ninja generator

from lib_util import cxx_findfiles

def gen_cmake(all_files, defines, includedirs, prj_name, buildfox_name, filename = "CMakeLists.txt"):
	text = r"""# generated by BuildFox
cmake_minimum_required(VERSION 2.8.3)
project(%s)
include_directories("%s")
add_custom_target(
  build
  ALL ninja
  WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}
  SOURCES "%s"
)
"""
	all_files = [buildfox_name] + cxx_findfiles(all_files)
	includedirs = ["."] + includedirs

	with open(filename, "w") as f:
		f.write(text % (
			prj_name,
			";".join(includedirs),
			";".join(all_files)
		))