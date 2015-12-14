package com.nourriture.app.setting;

import android.content.Context;
import android.content.Intent;
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
    private int[] picture = {R.drawable.name, R.drawable.account, R.drawable.password, R.drawable.sex, R.drawable.country, R.drawable.religion};
    private String[] list = {"Name", "Account", "Password", "Sex", "Country", "Religion"};

    private boolean is_two_pane;
    //private int user_id;  <TODO>

    ListView list_view_setting;
    List<Map<String, Object>> list_info = new ArrayList<>();
    SimpleAdapter adapter;

    @Override
    public void onAttach(Context context){
        super.onAttach(context);
        initInfo();
        adapter = new SimpleAdapter(context, list_info, R.layout.setting_list_item,
                new String[] {"header", "name", "value"},
                new int[] {R.id.header, R.id.name, R.id.value} );
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState){
        View view = inflater.inflate(R.layout.setting_list, container, false);
        list_view_setting = (ListView) view.findViewById(R.id.list_setting);
        list_view_setting.setAdapter(adapter);
        list_view_setting.setOnItemClickListener(this);

        return view;
    }

    @Override
    public void onActivityCreated(Bundle savedInstanceState){
        super.onActivityCreated(savedInstanceState);
        is_two_pane = (getActivity().findViewById(R.id.setting_layout) != null);
    }

    // Initialize the information of the user by user_id
    private void initInfo(){
        Map<String,String> result = new HashMap<>();
        String[] value = new String[6];

        // Get information from api and put it into <Map>result  (AJAX->MAP) <TODO>
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
    }

    @Override
    public void onItemClick(AdapterView<?> adapterView, View view, int i, long l){
        int position = (int) l;
        String clickItem = (String) list_info.get(position).get("name");
        String actionName = clickItem.toLowerCase();

        switch (actionName){
            case "name":
            {
                String name = (String) list_info.get(0).get("value");

                if (is_two_pane) {
                    //Use PersonalSettingNameFragment to replace the FrameLayout
                    //pass the name and isTwoPane to the fragment
                    Bundle arguments = new Bundle();
                    arguments.putString("name", name);
                    arguments.putBoolean("isTwoPane", is_two_pane);
                    PersonalSettingNameFragment personalSettingNameFragment = new PersonalSettingNameFragment();
                    personalSettingNameFragment.setArguments(arguments);
                    getActivity().getSupportFragmentManager().beginTransaction()
                            .replace(R.id.setting_layout, personalSettingNameFragment).commit();
                } else {
                    //start a new PersonalSettingNameActivity
                    //pass the name and isTwoPane to the activity and finally to the fragment
                    Intent intent = new Intent(getActivity(), PersonalSettingNameActivity.class);
                    intent.putExtra("name", name);
                    intent.putExtra("isTwoPane", is_two_pane);
                    startActivityForResult(intent, 0);
                }
                break;
            }

            case "account":
            {
                break;
            }

            case "password":
            {
                String password = (String) list_info.get(2).get("value");

                if (is_two_pane){
                    Bundle arguments = new Bundle();
                    arguments.putString("password", password);
                    arguments.putBoolean("isTwoPane", is_two_pane);
                    PersonalSettingPasswordFragment personalSettingPasswordFragment = new PersonalSettingPasswordFragment();
                    personalSettingPasswordFragment.setArguments(arguments);
                    getActivity().getSupportFragmentManager().beginTransaction()
                            .replace(R.id.setting_layout, personalSettingPasswordFragment).commit();
                } else {
                    Intent intent = new Intent(getActivity(), PersonalSettingPasswordActivity.class);
                    intent.putExtra("password", password);
                    intent.putExtra("isTwoPane", is_two_pane);
                    startActivityForResult(intent, 0);
                }
                break;
            }

            case "sex":
            {
                String sex = (String) list_info.get(3).get("value");

                if (is_two_pane){
                    //Use PersonalSettingSexFragment to replace the FrameLayout
                    //pass the sex and isTwoPane to the fragment
                    Bundle arguments = new Bundle();
                    arguments.putString("sex", sex);
                    arguments.putBoolean("isTwoPane", is_two_pane);
                    PersonalSettingSexFragment personalSettingSexFragment = new PersonalSettingSexFragment();
                    personalSettingSexFragment.setArguments(arguments);
                    getActivity().getSupportFragmentManager().beginTransaction()
                            .replace(R.id.setting_layout, personalSettingSexFragment).commit();
                } else {
                    //start a new PersonalSettingSexActivity
                    //pass the sex and isTwoPane to the activity and finally to the fragment
                    Intent intent = new Intent(getActivity(), PersonalSettingSexActivity.class);
                    intent.putExtra("sex", sex);
                    intent.putExtra("isTwoPane", is_two_pane);
                    startActivityForResult(intent, 0);
                }
            }

            case "country":
            {
                break;
            }

            case "religion":
            {
                break;
            }
        }
    }

    @Override
    public void onActivityResult(int requestCode, int resultCode, Intent intent){
        if (requestCode == 0) {
            if (resultCode == 0 || resultCode == 2 || resultCode == 3
                    || resultCode == 4 || resultCode == 5) {
                if ( intent != null ) {
                    Bundle data = intent.getExtras();
                    String value = data.getString(list[resultCode].toLowerCase());
                    changeValue(resultCode, value);
                }
            }
        }
    }

    public void changeValue(int index, String value){
        Long time = System.currentTimeMillis();
        System.out.println("Function:changeValue--[" + list_info.get(index).get("name") + ":" + value + "]");
        list_info.get(index).put("value", value);
        adapter.notifyDataSetChanged();
//        Post the new info to api <TODO>
//        String name = (String) list_info.get(0).get("value");
//        String account = (String) list_info.get(0).get("value");
//        String password = (String) list_info.get(0).get("value");
//        String sex = (String) list_info.get(0).get("value");
//        String country = (String) list_info.get(0).get("value");
//        String religion = (String) list_info.get(0).get("value");
        System.out.println("[time:" + (System.currentTimeMillis()-time) + "ms]");
    }
}
