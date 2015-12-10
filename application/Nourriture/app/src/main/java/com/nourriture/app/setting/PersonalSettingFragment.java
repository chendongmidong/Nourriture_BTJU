package com.nourriture.app.setting;

import android.content.Context;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.ListView;
import android.widget.SimpleAdapter;
import com.nourriture.app.R;

import java.util.*;

/**
 * Created by liuyifan on 15/12/10.
 */
@SuppressWarnings("unchecked")
public class PersonalSettingFragment extends Fragment implements AdapterView.OnItemClickListener {
    private int[] picture = {R.mipmap.name, R.mipmap.account, R.mipmap.password, R.mipmap.sex, R.mipmap.country, R.mipmap.religion};
    private String[] list = {"Name", "Account", "Password", "Sex", "Country", "Religion"};
    private String[] value = new String[6];

    private boolean isTwoPane;

    ListView list_setting1;
    List<Map<String, Object>> list_info;
    SimpleAdapter adapter;

    @Override
    public void onAttach(Context context){
        super.onAttach(context);
        list_info = getInfo(111);
        adapter = new SimpleAdapter(context, list_info, R.layout.setting_list_item,
                new String[] {"header", "name", "value"},
                new int[] {R.id.header, R.id.name, R.id.value} );
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState){
        View view = inflater.inflate(R.layout.setting_list, container, false);
        list_setting1 = (ListView) view.findViewById(R.id.list_setting);
        list_setting1.setAdapter(adapter);
        list_setting1.setOnItemClickListener(this);

        return view;
    }

    @Override
    public void onActivityCreated(Bundle savedInstanceState){
        super.onActivityCreated(savedInstanceState);
        isTwoPane = (getActivity().findViewById(R.id.setting_layout) != null);
    }

    // get personal information by userId
    private List getInfo(int userId){
        int id = userId;
        Map<String,String> result = new HashMap<>();
        List<Map<String, Object>> list_info = new ArrayList<>();

        // get information from api and put it into result  (AJAX->MAP) <TODO>
        result.put("name","Alice");
        result.put("account","Alice@gmail.com");
        result.put("password","Alice123");
        result.put("sex","female");
        result.put("country","China");
        result.put("religion","Empty");

        value[0] = result.get("name");
        value[1] = result.get("account");
        value[2] = result.get("password");
        value[3] = result.get("sex");
        value[4] = result.get("country");
        value[5] = result.get("religion");

        for(int i = 0; i < list.length; i++){
            Map<String, Object> listItem = new HashMap<>();
            listItem.put("header",picture[i]);
            listItem.put("name",list[i]);
            listItem.put("value",value[i]);
            list_info.add(listItem);
        }

        return list_info;
    }

    @Override
    public void onItemClick(AdapterView<?> adapterView, View view, int i, long l){
        int position = (int) l;
        String clickItem = (String)list_info.get(position).get("name");
        String actionName = clickItem.toLowerCase();

        if(isTwoPane) {
            if (actionName.equals("name")){
                String name = value[0];
                Bundle arguments = new Bundle();
                arguments.putString("name",name);
                PersonalSettingNameFragment personalSettingNameFragment = new PersonalSettingNameFragment();
                personalSettingNameFragment.setArguments(arguments);
                getActivity().getSupportFragmentManager().beginTransaction()
                        .replace(R.id.setting_layout, personalSettingNameFragment).commit();
            }
        } else {
            if (actionName.equals("name")){
                String name = value[0];
                PersonalSettingNameActivity.actionStart(getActivity(), name);
            }
        }
    }
}
